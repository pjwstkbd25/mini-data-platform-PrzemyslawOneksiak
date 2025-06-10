from helpers.argparser import Parser
from helpers.utils import file_reader, load_secret_password
from services.SQL import SQL
import os

def main():
    args = Parser().parse()
    csv_dir = args.csv_dir
    sql = SQL(
        user="postgres",
        password = load_secret_password("/run/secrets/postgres_password"),
        # password=args.password,
        host="postgres",
        db_name="bigdata",
        port="5432"
    )
    print("DEBUG: engine utworzony, próbuję load_data…")
    print(os.listdir(csv_dir))
    for fname in os.listdir(csv_dir):
        if not fname.lower().endswith(".csv"):
            continue
        table = os.path.splitext(fname)[0]
        full_path = os.path.join(csv_dir, fname)
        df = file_reader(full_path)
        print(df)
        sql.load_data(df, table)



if __name__ == "__main__":
    main()
