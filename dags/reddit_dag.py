import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args ={
    'owner' : 'codewithRaghav',
    'start_date' : datetime(2025,10,10),
}

file_postfix = datetime.now().strtime("%Y%m%d")

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args='default_args',
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
        'limits':100 

    }

)