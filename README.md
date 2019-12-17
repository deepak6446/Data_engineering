## 1. Sending email using aws ses (simple email service)
[Wsing Boto3](https://github.com/deepak6446/Data_engineering/blob/master/mail_send_boto3/send_mail_boto3.py)

## 2. Prestro Cluster on emr, use hive metastore to run queries on parquet in s3 and connect to Sisence or Tablue using JDBC
[Todo](https://github.com/deepak6446/Data_engineering/tree/master/presto_config_aws_emr): Automate spinup and shutdown using lambda service and bootup script in EMR.

## 3. Spark jobs
[Connect s3 and Read File from s3 in Spark](https://github.com/deepak6446/Data_engineering/blob/master/test_programmes/connect_s3_using_keys.py)

## 4. Recursive function to flatten data and replace special chars
[Functions](https://github.com/deepak6446/Data_engineering/blob/master/test_programmes/cleaning_data_rec_json.py)

## 5. Airflow scheduling jobs with airflow docker
ETL process to load data from s3 flatten and load in athena.
[DAGS](https://github.com/deepak6446/Data_engineering/blob/master/Airflow_Docker/airflow/dags/rcs_mongo_to_s3.py)
[Load Data from MongoDB](https://github.com/deepak6446/Data_engineering/blob/master/Airflow_Docker/airflow/dags/python/rcs_mongo_to_s3.py)
