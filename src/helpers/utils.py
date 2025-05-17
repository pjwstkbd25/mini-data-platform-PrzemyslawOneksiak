import pandas as pd


def file_reader(path):
    df = pd.read_csv(path)
    return df
