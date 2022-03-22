#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 22:28:40 2022

@author: francisrod01
"""

from pyspark import SparkContext
if __name__ == "__main__":
    sc = SparkContext("local", "PySpark example - Dataproc challenge")
    words = sc.textFile("./book-asset.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)

    wordCounts.saveAsTextFile("./results")
