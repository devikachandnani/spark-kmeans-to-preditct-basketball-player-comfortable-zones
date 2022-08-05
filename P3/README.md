# Lab 2: Part 3

## NY Parking Validations 

Based on the NY Parking Violation data, we need to figure out When tickets are most likely to be issued using a Spark environment and explore parallism

## Design 

This question asks to implement the same file with different levels of paralellism, specifically when those levels are set at 2,3,4 and 5. We set parellelism in the test.sh file by using the command:
```python
--conf spark.default.parallelism = 2
```

We adjust the final numerical value and set it to `2, 3, 4, and 5` by running the test.sh file four times and compare the time taken.

## Execution and Implementation
1. Update the manager and worker to your nodes' IP.
2. Configure your 3-node cluster so that they can login without using password.
3. Upload the data file named `nyparking_violations.csv` into the folder `test-data` by following the path 
```python
user_name@node-0:/spark-examples/test-data/
```
4. Next, upload `test.sh` and `P3.py` into a new folder within `test-python` with the path
```python
user_name@node-0:/spark-examples/test-python/lab2/P3
```
4. Run using the `test.sh` file using the bash command.

## Output
The program converges and returns the time when tickets are most likely to be issued.
