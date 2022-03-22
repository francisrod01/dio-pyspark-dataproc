#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:44:25 2022

@author: francisrod01
"""

from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()
df = spark.read.text("./book-asset.txt")
df = df.filter(F.col("value") != "") # Remove empty rows

word_counts = (
    df
        .withColumn("word", F.explode(F.split(F.col("value"), "\s+")))
        .withColumn("word", F.regexp_replace("word", "[^\w]", ""))
        .groupBy("word")
        .count()
        .sort("count", ascending=False)
)

# Top 10
word_counts.show(10)

# All words count
word_counts.agg(F.sum("count").alias("count_all_words")).show()

# Whale count
word_counts.filter(F.col("word").rlike("(?i)whale")).agg(
    F.sum("count").alias("whale_count")
).show()

# Unique count
print("Unique words: ", word_counts.count())
