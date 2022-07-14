from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator

@dag(start_date=datetime(2021, 1, 1),schedule_interval="@daily", catchup=False)

def dag_25():
	op = DummyOperator(task_id="task")

dag = dag_25()