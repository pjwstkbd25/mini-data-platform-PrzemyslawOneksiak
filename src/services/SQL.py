from pandas import DataFrame
from sqlalchemy import create_engine
import pandas as pd

class SQL:

    def __init__(self, user: str, password: str, host, db_name: str, port: str):
        self.engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
        print(f"DEBUG: host={host}, port={port}, password={password!r}, user={user}, db_name={db_name}")

    def load_data(self, data: DataFrame, table_name: str):
        data.to_sql(table_name, con=self.engine, if_exists="replace")

    def select_data(self, table_name, columns: list):
        try:
            pd.read_sql_query(f"SELECT {columns} FROM {table_name}", con=self.engine)
        except Exception as e:
            print(e)

