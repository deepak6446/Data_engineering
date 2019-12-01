# run using command
# spark-submit spark_submit_pyspark.py 

from pyspark import SparkContext, SparkConf

# create Spark context with Spark configuration
conf = SparkConf().setAppName("Deepak_1ST_job")
sc = SparkContext(conf=conf)

print("KATEEL")
