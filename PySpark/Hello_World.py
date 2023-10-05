from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

print("Hello World")

spark.stop()
