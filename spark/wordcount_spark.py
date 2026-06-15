import time
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("WordCount").setMaster("local[4]")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

start = time.time()

lines = sc.textFile("data/big_input.txt")

counts = lines.flatMap(lambda line: line.lower().split()) \
              .map(lambda word: (word.strip(",.!?;:()"), 1)) \
              .reduceByKey(lambda a, b: a + b)

result = counts.sortBy(lambda x: x[1], ascending=False).collect()

duration = round(time.time() - start, 3)

with open("results/output_spark.txt", "w") as f:
    for word, count in result:
        f.write(f"{word}: {count}\n")

print(f" Spark terminé en {duration} secondes")
print("Top 5 mots :")
for word, count in result[:5]:
    print(f"  {word}: {count}")