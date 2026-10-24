import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5)

filepath_ = './Datasets/winemag-data-130k-v2.csv'
filedata_ = pd.read_csv(filepath_, index_col=0)

# We can apply summary functions to single columns as well
# Example should be applying the describe to a col "Description"
col_desc = filedata_.winery.describe()

print(col_desc)