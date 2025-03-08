import csv
import pandas as pd
from src.helpers.argparser import Parser


def file_reader():
    args = Parser().parse()
    df = pd.read_csv(args.path)
    return df