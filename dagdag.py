import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="AIRFLOWTEAMDAG",
    start_date=datetime.datetime(2024, 1, 1),
    schedule="@daily",
)

EmptyOperator(task_id="task", dag=my_dag)
