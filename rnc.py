import pandas as pd
import numpy as np

filepath_ = './Datasets/winemag-data-130k-v2.csv'
filedata_ = pd.read_csv(filepath_)

canadian_ft = './Datasets/CAvideos.csv'
canadian_dt = pd.read_csv(canadian_ft)

british_ft  = './Datasets/GBvideos.csv'
british_dt = pd.read_csv(british_ft)

# To change the points column in our dataset to score
filedata_.rename(columns={'points' : 'score'})

# We can rename some elements of the index
filedata_.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# You'll probably rename columns very often, but rename index
# values very rarely. For that, set_index() is usually more convenient
#filedata_.set_index()

# Both the row index and the column index can have their own name attribute. 
# The complimentary rename_axis() method may be used to change these names.
filedata_.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# We will sometimes need to combine different DataFrames and/or Series in non-trivial ways
# If we want to study multiple countries simultaneously, we can use concat() to smush them together
combo = pd.concat([canadian_dt, british_dt])

# join() lets you combine different DataFrame objects which have an index in common. 
# For example, to pull down videos that happened to be trending on the same day in both Canada and the UK, we could do the following:
left = canadian_dt.set_index(['title', 'trending_date'])
right = british_dt.set_index(['title', 'trending_date'])

new_combo = left.join(right, lsuffix='_CAD', rsuffix='_UK')
print(combo.head())