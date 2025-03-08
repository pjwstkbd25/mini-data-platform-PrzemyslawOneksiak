from pandas import DataFrame
from sqlalchemy import create_engine
import pandas as pd

class SQL:

    def __init__(self, path):
        self.engine = create_engine(path)


    def load_data(self, data: DataFrame, table_name: str):
        data.to_sql(table_name, con=self.engine, if_exists="replace")

    def select_data(self, table_name, columns: list):
        pd.read_sql_query(f"SELECT {columns} FROM {table_name}", con=self.engine)

