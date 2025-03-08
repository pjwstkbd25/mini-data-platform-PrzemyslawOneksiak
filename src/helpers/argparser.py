import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("csv_path", type=str)
        self.parser.add_argument("db_path", type=str)

    def parse(self):
        try:
            self.parser.parse_args()
        except FileNotFoundError as e:
            print(e)
