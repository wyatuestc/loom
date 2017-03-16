#!/bin/bash

cd
. run.sh -q
spark-submit --class com.github.ehiggs.spark.terasort.TeraGen --executor-memory 75G /home/ubuntu2/software/spark-terasort/target/spark-terasort-1.0-jar-with-dependencies.jar 25g hdfs://10.10.1.2:9020/terasort_in