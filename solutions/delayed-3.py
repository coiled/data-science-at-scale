
import glob
import pandas as pd
from dask import delayed

# Use delayed to make a lazy version of Pandas' read_csv
read_csv_delayed = delayed(pd.read_csv)

def read_csv_parallel(files):
    # Lazily load each CSV file
    dfs = [read_csv_delayed(f) for f in files]
    # Concatenate the DataFrame pieces into a single DataFrame
    df = delayed(pd.concat)(dfs)
    return df

# Get list of CSV files and load them in paralell
files = glob.glob("data/nycflights/*.csv")
df = read_csv_parallel(files)
%time df.compute()