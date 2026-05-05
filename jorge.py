from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    #'retries': 1,
    #'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='pruebasgit',
    default_args=default_args,
    description='Ejecuta nc para chequear puerto desde el webserver',
    start_date=datetime(2025, 9, 5),
    schedule=None,
    catchup=False,
    tags=["Jorge"],
) as dag:

    #########################################################
    # Tarea principal: ejecuta el comando "nc"              #
    #########################################################
    netcat_task1 = BashOperator(
        task_id='run_netcat_check1',
        bash_command='nc -zv 10.203.109.182 1538',
        #on_failure_callback=notify_failure,
    )

    netcat_task2 = BashOperator(
        task_id='run_netcat_check2',
        bash_command='nc -zv 10.203.109.183 1538',
        #on_failure_callback=notify_failure,
    )

    netcat_task3 = BashOperator(
        task_id='run_netcat_check3',
        bash_command='nc -zv 10.203.109.184 1538',
        #on_failure_callback=notify_failure,
    )

    netcat_task4 = BashOperator(
        task_id='run_netcat_check4',
        bash_command='nc -zv 192.168.235.92 445',
        #on_failure_callback=notify_failure,
    )  


    netcat_task5 = BashOperator(
        task_id='run_netcat_check5',
        bash_command='echo ejemplo tarea de prueba',
        #on_failure_callback=notify_failure,
    )  
