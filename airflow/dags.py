#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-11-18
Author: @danvargg
"""

import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def greet():
    """Greet function"""
    logging.info('hello, hello')


dag = DAG(
    'test_00',
    start_date=datetime.datetime.now()
)

greet_task = PythonOperator(  # Node
    task_id='greeting',
    python_callable=greet,
    dag=dag
)
