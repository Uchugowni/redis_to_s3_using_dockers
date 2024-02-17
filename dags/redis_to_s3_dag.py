import airflow
from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_arg={
    'owner':'Uchugowni Giribabu',
    'start_date':datetime(2023, 10, 22)
}

file_postfix=datetime.now().strftime("%Y%m%d")

dag=DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_arg,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline']
)

#Extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddis_pipeline,
    op_kwargs={
        'filename':f'reddit_{file_postfix}',
        'subreddit':'dataengineering',
        'time_filter': 'day',
        'limit':100
    }
)

#upload to s3
