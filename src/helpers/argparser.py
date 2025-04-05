import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--csv_path", type=str, required=True, help="Ścieżka do pliku CSV")
        self.parser.add_argument("--table_name", type=str, required=True, help="Nazwa tabeli w bazie")
        self.parser.add_argument("--password", type=str, required=True, help="Hasło do postgreSQL")

    def parse(self):
        try:
            return self.parser.parse_args()
        except FileNotFoundError as e:
            print(e)
