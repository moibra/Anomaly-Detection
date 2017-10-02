import pandas as pd

dataframes = [pd.read_csv(p) for p in ("test1.csv", "test2.csv")]

merged_dataframe = pd.concat(dataframes, axis=0)

 # merged_dataframe.to_csv("merged.csv")