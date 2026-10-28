import pandas as pd
import numpy as np

filepath_ = './Datasets/winemag-data-130k-v2.csv'

filedata_ = pd.read_csv(filepath_, index_col=0)

# Replicating the value_count() function, groupwise analysis
# Original value_count fuunction
val_count = filedata_.value_counts(['points'])

# Using groupwise_analysis
# I think here the Series creates a name, Points
val_group = filedata_.groupby('points').points.count()
val_group = filedata_.groupby('points').size() # This also has the same function has the same output as the code above

# We can also use summary functions with the above function
price_group = filedata_.groupby('points').price.min()

# Here's one way of selecting the name of the first wine reviewed 
# from each winery in the dataset:
winery = filedata_.groupby('winery').apply(lambda df: df.title.iloc[0])

# For even more fine-grained control, you can also group by more than one column
col2 = filedata_.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# We can generate a simple statistical summary of the dataset as follows:
summary = filedata_.groupby(['country']).price.agg([len, min, max])

# The multi-index method you will use most often is the one for 
# converting back to a regular index, the reset_index() method:
index_reset = summary.reset_index()

# That is to say, when outputting the result of a groupby, the order of the rows 
# is dependent on the values in the index, not in the data. To get data in the order 
# want it in we can sort it ourselves. The sort_values() method is handy for this.
sort_index = index_reset.sort_values(by='len')

# sort_values() defaults to an ascending sort, where the lowest values go first. 
# However, most of the time we want a descending sort, where the higher numbers go first
sort_asc = index_reset.sort_values(by='len', ascending=False)

# To sort by index values, use the companion method sort_index(). 
# This method has the same arguments and default order:
sort_index = index_reset.sort_index()

# Finally, know that you can sort by more than one column at a time:
sort_by2 = index_reset.sort_values(by=['country', 'len'])

print(filedata_.head())