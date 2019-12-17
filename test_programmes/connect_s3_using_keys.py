# run using command
# time spark-submit --packages org.apache.hadoop:hadoop-aws:3.2.1 connect_s3_using_keys.py

from pyspark import SparkContext, SparkConf
import ConfigParser
import pyspark

# create Spark context with Spark configuration
conf = SparkConf().setAppName("Deepak_1ST_job")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

hadoop_conf = sc._jsc.hadoopConfiguration()

config = ConfigParser.ConfigParser()
config.read("/home/deepak/Desktop/secure/awsCred.cnf")
accessKeyId = config.get("aws_keys", "access_key")
secretAccessKey = config.get("aws_keys", "secret_key")

hadoop_conf.set(
    "fs.s3n.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("fs3a.access.key", accessKeyId)
hadoop_conf.set("s3a.secret.key", secretAccessKey)

sqlContext = pyspark.SQLContext(sc)

df = sqlContext.read.csv(
    "s3a://bucket/filepath")
df.show()

print("KATEEL")
