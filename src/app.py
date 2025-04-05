from src.helpers.argparser import Parser
from src.helpers.provider import file_reader
from src.services.SQL import SQL

def main():
    args = Parser().parse()
    df = file_reader(args.csv_path)
    sql = SQL(
        user="postgres",
        password = args.password,
        host="localhost",
        db_name="bigdata",
        port="5433"
    )
    sql.load_data(df, args.table_name)



if __name__ == "__main__":
    main()
