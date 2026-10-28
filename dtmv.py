import pandas as pd
import numpy as np

filepath_ = './Datasets/winemag-data-130k-v2.csv'
filedata_ = pd.read_csv(filepath_, index_col=0)

# You can use the dtype property to grab the type of a specific column.
price_type = filedata_.price.dtype

# We may transform the points column from its existing int64 data type into a float64
filedata_.points.astype('float64')

# Pandas provides some methods specific to missing data
ctry = filedata_[pd.isnull(filedata_.country)]

# We can simply replace each NaN with an "Unknown":
filedata_.region_2.fillna("Unknown")

# Backfill means filling a missing value (NaN) with the next available non-missing value below it in a column.
filedata_.region_2.bfill()

# Forward fill Looks up the column for the previous available value.
filedata_.region_1.ffill()
print(price_type)