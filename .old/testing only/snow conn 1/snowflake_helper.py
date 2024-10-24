import os
import logging

import pandas as pd
import sqlalchemy
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from snowflake.snowpark import Session
from snowflake.connector.pandas_tools import pd_writer

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s')
ape_logger = logging.getLogger("Aperture")
ape_logger.setLevel(logging.INFO)


ACCOUNT='fla16248.east-us-2.azure'


class SnowFlakeConnection():
    def __init__(self, config: dict={}):
        self.account=ACCOUNT
        self.user=config.get('user', os.getenv('SNOWFLAKE_USER'))
        self.password=config.get('password', os.getenv('SNOWFLAKE_PASSWORD'))
        self.database=config.get('database', 'APERTURE')
        self.warehouse=config.get('warehouse', 'MAIN_WH')
        self.schema = config.get('schema', 'PUBLIC')
        self.role='ACCOUNTADMIN'

    @property
    def engine(self):
        return create_engine(URL(
                                account=self.account,
                                user=self.user,
                                password=self.password,
                                database=self.database,
                                role=self.role,
                                warehouse=self.warehouse,
                            )).execution_options(autocommit=True)

    @property
    def connection_config(self):
        return {
                "user": self.user,
                "password": self.password,
                "account": self.account,
                "database": self.database,
                "schema": self.schema,
                "role": self.role,
                "warehouse":self.warehouse,
            }

    @property
    def snowflake_session(self):
        return Session.builder.configs(self.connection_config).create()
    
    def session_write_df(self, **kwargs):
        ape_logger.info(f"Executing: {kwargs}")
        return self.snowflake_session.write_pandas(**kwargs)
    
    def session_read_df(self, **kwargs):
        ape_logger.info(f"Executing: {kwargs}")
        return self.snowflake_session.sql(**kwargs).to_pandas()

    def session_qry(self, **kwargs):
        ape_logger.info(f"Executing: {kwargs}")
        return self.snowflake_session.sql(**kwargs).collect()


def execute_snowflake_query(qry, db_conn):
    connection = db_conn.engine.connect()
    try:
        ape_logger.info(f"Executing {qry}")
        results = connection.execute(qry).fetchall()
        # connection.commit()
    except Exception as e:
        raise Exception(e)   
    finally:
        
        connection.close()
        db_conn.engine.dispose() 
    return results


def read_snowflake_df(qry, db_conn):
    ape_logger.info(f"Executing {qry}")
    return pd.read_sql_query(qry, db_conn.engine)


def write_df_to_snowflake(
        df: pd.DataFrame,
        table: str,
        schema: str,
        db_conn=None,
        if_exists: str = 'append',
        index: bool = False) -> None:
    """Writes rows to SQL DB"""
    with db_conn.engine.connect() as conn:
        ape_logger.info(f"Loading {len(df)} row to SF.")
        df.to_sql(table, conn, schema=schema, if_exists=if_exists, index=index)


