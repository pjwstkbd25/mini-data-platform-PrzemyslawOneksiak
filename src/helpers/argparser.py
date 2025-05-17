import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--csv_dir", type=str, required=True, help="Ścieżka do katalogu z CSV")
        self.parser.add_argument("--password", type=str, required=True, help="Hasło do postgreSQL")

    def parse(self):
        try:
            return self.parser.parse_args()
        except FileNotFoundError as e:
            print(e)
