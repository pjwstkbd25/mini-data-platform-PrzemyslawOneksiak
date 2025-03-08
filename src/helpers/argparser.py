import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("csv_path", type=str)
        self.parser.add_argument("db_path", type=str)
        self.parser.add_argument("table_name", type=str)

    def parse(self):
        try:
            return self.parser.parse_args()
        except FileNotFoundError as e:
            print(e)
