#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-09-21
Author: @danvargg
"""
import numpy as np
import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri
from sagemake.predictor import csv_serializer
from sagemaker.tuner import IntegerParameter, ContinuousParameter, HyperparameterTuner

# Session
session = sagemaker.Session()

# IAM role
role = get_execution_role()

# Upload files to S3
# S3 bucket prefinx
prefix = 'data_folder'
train_location = session.upload_data(DATA_DIR, key_prefix=prefix)
val_location = session.upload_data(DATA_DIR, key_prefix=prefix)
test_location = session.upload_data(DATA_DIR, key_prefix=prefix)

# Build container
container = get_image_uri(session.boto_region_name, 'xgboost')

# Estimator
xgb = sagemaker.estimator.Estimator(
    container, role,
    train_instance_count=1, train_instance_type='ml.m4.xlarge',
    output_path=f's3://{session.default_bucket()}/{prefix}/output',
    sagemaker_session=session)

# Hyperparameters optimization
xgb.set_hyperparameters(
    max_depth=5, eta=0.2, gamma=4, min_child_weight=6, subsample=0.8, objective='reg:linear',
    early_stopping_rounds=10, num_round=200)

# Model training
s3_input_train = sagemaker.s3_input(s3_data=train_location, content_type='csv')
s3_input_val = sagemaker.s3_input(s3_data=val_location, content_type='csv')

xgb.fit({'train': s3_input_train, 'validation': s3_input_val})

# Test model (Sagemaker batch transform)
xgb_transformer = xgb.transformer(
    instance_count=1, instance_tpe='ml.m4.xlarge')
xgb_transformer.transform(
    test_location, content_type='text/csv', split_type='Line')

# Job process
xgb_transformer.wait()

# Save output locally
# !aws s3 cp --recursive $ xgb_transformer.output_path $data_dir

# Clean up resources on notebook instance
# Remove files and dir
# !rm $data_dir/* && rmdir $data_dir

# Deploy model
xgb_predictor = xgb.deploy(initial_instance_count=1,
                           instance_type='ml.m4.xlarge')

# Test the deployed moel
xgb_predictor.content_type = 'text/csv'
xgb_predictor.csv_serializer = csv_serializer

y_pred = xgb_predictor.predict(X_test.values).decode('utf-8')
y_pred = np.fromstring(y_pred, sep=',')

# delete endpoint
xgb_predictor.delete_endpoint()

# Manual process
# Serialize input data
payload = [[str(entry) for entry in row] for row in X_test.values]
payload = '\n'.join([','.join(row) for row in payload])

# Invoke the endpoint
response = session.sagemaker_runtime_client.invoke_endpoint(
    EndpointName=endpoint_name, ContentType='text/csv', Body=payload)

# Deserialize for endpoint call
result = response['Body'].read().decode('utf-8')
y_pred = np.fromstring(result, sep=',')

# Delete endpoint
session.sagemaker_client.delete_endpoint(EndpointName=endpoint_name)

# Use endpoint
runtime = boto3.Session().client('sagemaker-runtime')

# Print endpoint info
xgb_predictor.endpoint
response = runtime.invoke_endpoint(
    EndpointName=xgb_predictor.endpoint, ContentType='text/csv',
    Body=','.join([str(val) for val in test_bow]).encode('utf-8'))
response = response['Body'].read().decode('utf-8')

xgb_predictor.delete_endpoint()

# Lambda function
# 1. Create an IAM role for the lambda function
# 2. Create function
# 3. Configure and test event (replace body)
# 4. Setup API gateway
# 5. Add actions (create method: post)
# 6. Deployment stage


def lambda_handler(event, context):
    result = response['Body'].read().decode('utf-8')
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain', 'Access-Control-Allow-origin': '*'},
        'body': str(result)
    }

# Request
# API gateway stages
# TODO: make manual request
# Delete endpoint, lambda function and API


# Hyperparameters optimization
xgb_hyperparameter_tuner = HyperparameterTuner(
    estimator=xgb, objective_metric_name='validation:rmse', objective_type= 'Minimize,
    max_jobs=20, max_parallel_jobs=3,
    hyperparameters_ranges={
        'max_depth': IntegerParameter(3, 12),
        'eta': ContinuousParameter(0.05, 0.5),
        'min_child_weight': IntegerParameter(2, 8),
        'subsample': ContinuousParameter(0.5, 0.9),
        'gamma': ContinuousParameter(0, 10)
    })

# Best hyperparams
xgb_hyperparameter_tuner.best_training_job()
