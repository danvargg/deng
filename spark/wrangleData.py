#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2020-10-28
Author: @danvargg
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, desc, asc
from pyspark.sql.functions import sum as Fsum
from pyspark.sql.types import StringType, IntegerType

spark = SparkSession.builder.appName('wrangle data').getOrCreate()

data = spark.read.json('/home/daniel/innodem/input/input.json')

print(data.count())

print(data.head())
# Does not work
# print(data.printSchema('deviceDetails').show())

# Query
# data.select(['column', 'column']).where(data.row == 'whatever').collect()

# To pandas
df = data.toPandas()

# Create a view first
data.createOrReplaceTempView('table')

# Spark SQL
spark.sql('SELECT * FROM table LIMIT 2')

spark.sql(
    """
    SELECT *
    FROM table
    LIMIT 2
    """
).show()  # or collect
