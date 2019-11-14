# presto-parquet-files-aws-emr
How to configure prestro cluster on emr and use hive metastore to run queries on parquet in s3 

# what is presto:
Presto is a distributed SQL query engine optimized for ad hoc analysis. It supports the ANSI SQL standard, including complex queries, aggregations, joins, and window functions. Presto can run on multiple data sources, including Amazon S3.

## step1: create an emr instance
EMR cluster on amazon is preconfigured to install presto and hive (just select advance while configuring instance and select apps)
select number of worker nodes

## step2: configure DB using hive meta store
- follow following commands inside presto master node
--> hive
--> CREATE EXTERNAL TABLE `table_name`(
        >   `field_1` string,
        >   `field_2` string,
        )
    > ROW FORMAT SERDE
    >   'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
    > STORED AS INPUTFORMAT
    >   'org.apache.hadoop.mapred.TextInputFormat'
    > OUTPUTFORMAT
    >   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    > LOCATION
    >   's3://sample.db/table_name'
    > TBLPROPERTIES (
    >   'has_encrypted_data'='false',
    >   'transient_lastDdlTime'='1572331300');

--> exit()
--> presto
--> use hive.default;   (use hive meta store)

## step3: update security policy
update security policies for inbound ports to open port 8889 and ip of instance from which request will come to master node in emr.

## step4: query using python script or JDBC driver
change IP and Port in connect_presto_db.py and run using python connect_presto_db.py
or look in file sisence_connect_jdbc_to_query_using jdbc


