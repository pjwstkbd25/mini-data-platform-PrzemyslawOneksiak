import pandas as pd


def file_reader(path):
    df = pd.read_csv(path)
    return df

def load_secret_password(path):
    with open(path) as f:
        return f.read().strip()