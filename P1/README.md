# Lab 2: Part 1 

## NBA Shot Logs

This question requires implementing the K-Means algorithm using Spark!

For each player, we define the comfortable zone as, 

{SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}

The assignment asks to develop an K-Means algorithm to classify each player’s records into 4 comfortable zones. We mst consider the hit rate to find out which zone is the best for James Harden, Chris Paul, Stephen Curry and Lebron James.

## Design

We will be using an RDD based iteration, like the question asks, we transform the previous RDD inot a new one for the next iteration.

## Execution and Implementation
1. Update the manager and worker to your nodes' IP.
2. Configure your 3-node cluster so that they can login without using password.
3. Upload the data file named `shot_logs.csv` into the folder `test-data` by following the path 
```python
user_name@node-0:/spark-examples/test-data/
```
4. Next, upload `test.sh` and `P1.py` into a new folder within `test-python` with the path
```python
user_name@node-0:/spark-examples/test-python/lab2/P1
```
4. Run using the `test.sh` file using the bash command.

## Output
The program converges and returns the four Final Centroids in the format [[x1,y1,z1], [x2,y2,z2], [x3,y3,z3], [x4,y4,z4]].




