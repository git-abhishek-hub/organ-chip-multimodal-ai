import pandas as pd

metadata = pd.read_parquet(r"E:\organ-chip-ai\data\raw\cell_painting\metadata.parquet")
index= pd.read_parquet(r"E:\organ-chip-ai\data\raw\cell_painting\index.parquet")
print(metadata.shape)
print(index.shape)
metadata.head()
print (metadata.columns)
print(metadata.head(10))