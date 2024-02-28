from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'izayah.com',
    'start_date': datetime(2024, 2, 28),
    'catchup': False
}

dag = DAG(
    'hello_world',
    default_args= default_args,
    schedule=timedelta(day=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command='echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_izayah',
    bash_command='echo "Hello From Izayah"',
    dag = dag
)

t1 >> t2