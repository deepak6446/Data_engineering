# airflow dag
# This file contains code to push data to s3 from mongo
# data will not be saved in local and will be send as a stringified json

from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 7, 11),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 72,
    'retry_delay': timedelta(hours=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'adhoc':False,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}

dag = DAG(
    'rcs_mongo_to_s3',
    catchup=True,   # rerun all task until the catch up is finised (make false after all schedule till current date is finished)
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval="0 8 * * *",
)

# t1 is tasks created by instantiating operators
t1 = BashOperator(
    task_id='rcs_mongo_load_s3',
    bash_command="python3 /usr/local/airflow/dags/python/rcs_mongo_to_s3.py '{{ execution_date }}'",
    dag=dag,
)

t2 = BashOperator(
    task_id='rcs_mongo_databricks_api',
    bash_command="node /usr/local/airflow/dags/python/rcs_databricks_api.js '{{ execution_date }}'",
    dag=dag,
)

# execute t2 after t1
t1 >> t2