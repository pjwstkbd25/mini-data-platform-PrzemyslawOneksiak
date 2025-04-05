import csv
import pandas as pd
from src.helpers.argparser import Parser


def file_reader(path):
    df = pd.read_csv(path)
    return df

def load_secret_password(path):
    with open(path, 'r') as f:
        return f.read().strip()