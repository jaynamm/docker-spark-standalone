from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf()

conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = SparkSession.builder.config(conf=conf).getOrCreate()

data = spark.range(0, 5)
data.write.format("delta").save("./delta-table")