from datetime import datetime

import sql_ddl
from airflow.operators import (StageToRedshiftOperator)
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator

from airflow import DAG

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'udacity',
    'start_date': datetime(2020, 4, 16),
}

dag = DAG('udac_example_dag_v30',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow'
          )

start_operator_task = DummyOperator(task_id='Begin_execution', dag=dag)

create_stage_events_table_task = PostgresOperator(
    task_id="create_stage_event_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_ddl.CREATE_STAGE_EVENTS
)

stage_events_to_redshift_task = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    table="public.staging_events",
    s3_bucket="udacity-dend",
    s3_key="log_data"  # TODO import partitioned data
)

# stage_songs_to_redshift = StageToRedshiftOperator(
#     task_id='Stage_songs',
#     dag=dag
# )
#
# load_songplays_table = LoadFactOperator(
#     task_id='Load_songplays_fact_table',
#     dag=dag
# )
#
# load_user_dimension_table = LoadDimensionOperator(
#     task_id='Load_user_dim_table',
#     dag=dag
# )
#
# load_song_dimension_table = LoadDimensionOperator(
#     task_id='Load_song_dim_table',
#     dag=dag
# )
#
# load_artist_dimension_table = LoadDimensionOperator(
#     task_id='Load_artist_dim_table',
#     dag=dag
# )
#
# load_time_dimension_table = LoadDimensionOperator(
#     task_id='Load_time_dim_table',
#     dag=dag
# )
#
# run_quality_checks = DataQualityOperator(
#     task_id='Run_data_quality_checks',
#     dag=dag
# )

end_operator_task = DummyOperator(task_id='Stop_execution', dag=dag)

start_operator_task >> create_stage_events_table_task
create_stage_events_table_task >> stage_events_to_redshift_task
stage_events_to_redshift_task >> end_operator_task
