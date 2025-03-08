import csv
import pandas as pd
from src.helpers.argparser import Parser


def file_reader(path):
    df = pd.read_csv(path)
    return df