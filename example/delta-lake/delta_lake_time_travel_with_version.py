from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf()

conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = SparkSession.builder.config(conf=conf).getOrCreate()

data = spark.range(5, 10)
data.write.format("delta").mode("overwrite").save("./delta-table")

df = spark.read.format("delta").option("versionAsOf", 0).load("./delta-table")
df.show()