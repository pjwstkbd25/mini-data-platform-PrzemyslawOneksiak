from helpers.argparser import Parser
from helpers.utils import file_reader
from services.SQL import SQL
import os

def main():
    args = Parser().parse()
    csv_dir = args.csv_dir
    sql = SQL(
        user="postgres",
        password = args.password,
        host="localhost",
        db_name="bigdata",
        port="5433"
    )
    for fname in os.listdir(csv_dir):
        if not fname.lower().endswith(".csv"):
            continue
        table = os.path.splitext(fname)[0]
        full_path = os.path.join(csv_dir, fname)
        df = file_reader(full_path)
        sql.load_data(df, table)



if __name__ == "__main__":
    main()
