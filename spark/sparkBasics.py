#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-10-28
Author: @danvargg
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('first app').getOrCreate()

# Session Parameters
print(spark.sparkContext.getConf().getAll())

# Read json
data = spark.read.json('/home/daniel/innodem/input/input.json')

# Print file schema
data.printSchema()

# Describe the data
print(data.describe())

# Show a record
print(data.show(n=1))

# Show various records
print(data.take(5))

# Save in another format (does not work)
data.write.save(
    '/home/daniel/innodem/input/input.csv', format='csv', header=True)
