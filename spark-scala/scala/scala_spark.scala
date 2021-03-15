import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder.appName("spark on local").getOrCreate()

val data = Seq((1,2,3), (4,5,6), (6,7,8), (9,19,10))
val ds = spark.createDataset(data)
ds.show()


