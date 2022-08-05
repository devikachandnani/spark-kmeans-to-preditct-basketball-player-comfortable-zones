#!/usr/bin/env python
from __future__ import print_function
import sys
import math
from math import sqrt
from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.types import *

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("P1")\
        .getOrCreate()

def find_center(data, center):
	dictionary = [] 
	for c in center:
		val = 0.
		for i in range(3):
			val += (data[i] - c[i]) ** 2
		dist = sqrt(val)   
		dictionary.append(dist)   
	nearest_center = float('inf') 
	index = -1
	for i, v in enumerate(dictionary):
		if v < nearest_center:
			nearest_center = v
			index = i
	return int(index), data

def calculate_centroid(data):

	key, value = data[0], data[1]
	n = len(value)
	update = [0.] * 3
	for i in value:
		update[0] += float(i[0])
		update[1] += float(i[1])
		update[2] += float(i[2])
	closest_center = [round(x / n, 4) for x in update]
	return closest_center


df = spark.read.format("csv").load(sys.argv[1], header= True, inferSchema =True)
points = df.filter(df.player_name == 'james harden').select('SHOT_DIST','CLOSE_DEF_DIST', 'SHOT_CLOCK').na.drop()
r_dist_dataset = points.rdd.map(lambda r: (r[0], r[1], r[2]))

k = 4
FirstCentroid = r_dist_dataset.takeSample(False, k)
runNumber = 0 
PrevCentroid = FirstCentroid

for m in range(40):
	mapper_1 = r_dist_dataset.map(lambda x: find_center(x, PrevCentroid))
	reducer_1 = mapper_1.groupByKey()
	mapper_2 = reducer_1.map(lambda x: calculate_centroid(x)).collect()	
	CurrentCentroid = mapper_2
	converge = 0 
	for i in range(k):
		if CurrentCentroid[i] == PrevCentroid[i]:
			converge += 1
		else:
			diff = 0.0009 
			closeDiff = [round((a - b)**2, 6) for a, b in zip(CurrentCentroid[i], PrevCentroid[i])]
			if all(v <= diff for v in closeDiff):
				converge += 1

	if converge >= 4:
		print("In this program, converge happens at the %s iteration\n" %(runNumber))
		print("\nFinal Centroids: %s" %(CurrentCentroid))
		break
	
	else:
		runNumber += 1
		print("Iteration - %s round" %(runNumber))
		PrevCentroid = CurrentCentroid
		print('Update:',PrevCentroid,'\n')

spark.stop()
