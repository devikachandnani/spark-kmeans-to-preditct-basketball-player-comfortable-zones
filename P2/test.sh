#!/bin/bash
source ../../../env.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab2/P2/input/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab2/P2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../test-data/nyparking_violations.csv /lab2/P2/input/
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 ./P2.py hdfs://$SPARK_MASTER:9000/lab2/P2/input/
