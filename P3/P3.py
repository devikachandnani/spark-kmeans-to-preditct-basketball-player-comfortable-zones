#!/usr/bin/env python
from __future__ import print_function
import sys
from operator import add
from pyspark.sql import SparkSession
from  pyspark.sql.functions import col

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("P3")\
        .getOrCreate()

def calc_when(tup):
    date_month = tup[0]
    hours_time = tup[1]
    month = date_month[0:2]
    time = hours_time[0:2] + hours_time[-1]
    detail_day_time = month + "-" + time
    return (detail_day_time,1)


df = spark.read.format("csv").load(sys.argv[1], header = True, inferSchema=True)
df = df.select(col('Issue Date'), col('Violation Time'))
df = df.na.drop('any')    
df = df.rdd.map(lambda loop : (loop['Issue Date'],loop['Violation Time']))

new_df = df.map(lambda tup : calc_when(tup))
newer_df = new_df.reduceByKey(add)
newest_df = newer_df.sortBy(lambda tup : tup[1], ascending= False)

detail_day_time = newest_df.take(1)

add_numbers = detail_day_time[0][0].split('-')
month = add_numbers[0]
time = add_numbers[1]


print("Tickets are most likely to be issued at", time+"M")


spark.stop()
