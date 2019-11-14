# presto-parquet-files-aws-emr
How to configure prestro cluster on emr and use hive metastore to run queries on parquet in s3 

# what is presto:
Presto is a distributed SQL query engine optimized for ad hoc analysis. It supports the ANSI SQL standard, including complex queries, aggregations, joins, and window functions. Presto can run on multiple data sources, including Amazon S3.

## step1: create an emr instance
EMR cluster on amazon is preconfigured to install presto and hive (just select advance while configuring instance and select apps)
select number of worker nodes

## step2: configure DB using hive meta store
follow following commands inside presto master node </br>
--> hive </br>
--> CREATE EXTERNAL TABLE `table_name`( </br>
        >   `field_1` string, </br>
        >   `field_2` string, </br>
        ) </br>
    > ROW FORMAT SERDE </br>
    >   'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' </br>
    > STORED AS INPUTFORMAT </br>
    >   'org.apache.hadoop.mapred.TextInputFormat' </br>
    > OUTPUTFORMAT </br>
    >   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' </br>
    > LOCATION </br>
    >   's3://sample.db/table_name' </br>
    > TBLPROPERTIES ( </br>
    >   'has_encrypted_data'='false', </br>
    >   'transient_lastDdlTime'='1572331300'); </br>

--> exit() </br>
--> presto </br>
--> use hive.default;   (use hive meta store) </br>

## step3: update security policy </br>
update security policies for inbound ports to open port 8889 and ip of instance from which request will come to master node in emr. </br>

## step4: query using python script or JDBC driver </br>
change IP and Port in connect_presto_db.py and run using python connect_presto_db.py </br>
or look in file sisence_connect_jdbc_to_query_using jdbc </br>


