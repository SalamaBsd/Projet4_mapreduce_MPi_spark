import time
import csv
from pyspark import SparkContext, SparkConf

results = []

for data_file, label in [("data/input.txt", "small"), ("data/big_input.txt", "big")]:
    conf = SparkConf().setAppName("WordCount").setMaster("local[4]")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")

    start = time.time()
    counts = sc.textFile(data_file) \
               .flatMap(lambda l: l.lower().split()) \
               .map(lambda w: (w.strip(",.!?;:()"), 1)) \
               .reduceByKey(lambda a, b: a + b)
    counts.count()
    duration = round(time.time() - start, 3)

    sc.stop()
    results.append((label, duration))
    print(f"Spark [{label}] : {duration} secondes")

with open("results/bench_spark.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["taille", "temps_secondes"])
    writer.writerows(results)

print(" Benchmark Spark sauvegardé dans results/bench_spark.csv")