# Lab 2: Part 2

## NY Parking Validations 

Based on the NY Parking Violation data, given a Black vehicle parking illegally at 34510, 10030, 34050 (streat codes). What is the probability that it will get an ticket?

We will use a similar K-means algorithm as Part 1 to answer this question.

## Design 

The K-Means algorithm is implemented with PySpark by initializing the spark session and loading in the dataset as a dataframe. Then we will essentially filter the dataframe color to black using any possible verbiage for it, we then transofm the new filtered dataset into an RDD so we can iterate. We use the given street code and use K-means to count the cloesest centers to that address and calculate the probability using how many of them did get a ticket.


## Execution and Implementation
1. Update the manager and worker to your nodes' IP.
2. Configure your 3-node cluster so that they can login without using password.
3. Upload the data file named `nyparking_violations.csv` into the folder `test-data` by following the path 
```python
user_name@node-0:/spark-examples/test-data/
```
4. Next, upload `test.sh` and `P2.py` into a new folder within `test-python` with the path
```python
user_name@node-0:/spark-examples/test-python/lab2/P2
```
4. Run using the `test.sh` file using the bash command.

## Output
The program converges and returns the probability that the black vehicle will get a ticket if parked at given address.
