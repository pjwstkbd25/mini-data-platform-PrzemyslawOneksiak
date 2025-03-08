def main():
    args = Parser().parse()
    df = file_reader(args.csv_path)
    sql = SQL(args.db_path)
    sql.load_data(df, args.table_name)


if __name__ == "__main__":
    main()
