from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd, shutil

def ingest_orders():
    src = '/opt/airflow/data_generation/orders.csv'
    dst = f'/opt/airflow/data/bronze/orders_{datetime.now().date()}.csv'
    shutil.copy(src, dst)
    df = pd.read_csv(dst)
    print(f'Ingested {len(df)} rows into bronze layer')

with DAG(
    dag_id='batch_ingestion',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args={'retries': 2, 'retry_delay': timedelta(minutes=5)}
) as dag:
    ingest_task = PythonOperator(
        task_id='ingest_orders',
        python_callable=ingest_orders
    )
