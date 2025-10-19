import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args ={
    'owner' : 'codewithRaghav',
    'start_date' : datetime(2025,10,10),
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval = '@daily',
    catchup=False,
    tags= ['reddit', 'etl', 'pipeline']  # optional
)

# Extraction From Reddit

extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs ={
        'file_name' : f'reddit_{file_postfix}',
        'subreddit' : 'dataEngineering',
        'time_filter':'day',
        'limit':100 

    },
    dag=dag
)

# Upload to AWS S3 Bucket
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3