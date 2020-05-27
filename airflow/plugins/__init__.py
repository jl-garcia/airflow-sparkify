from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

# Defining the plugin class
from .helpers.sql_queries import SqlQueries
from .operators.data_quality import DataQualityOperator
from .operators.load_dimension import LoadDimensionOperator
from .operators.load_fact import LoadFactOperator
from .operators.stage_redshift import StageToRedshiftOperator


class UdacityPlugin(AirflowPlugin):
    name = "udacity_plugin"
    operators = [
        StageToRedshiftOperator,
        LoadDimensionOperator,
        LoadFactOperator,
        DataQualityOperator
    ]
    helpers = [
        SqlQueries
    ]
