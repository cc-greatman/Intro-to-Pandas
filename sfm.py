import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5)

filepath_ = './Datasets/winemag-data-130k-v2.csv'
filedata_ = pd.read_csv(filepath_, index_col=0)

# We can apply summary functions to single columns as well
# Example should be applying the describe to a col "Description"
# The output actually depends on the the datatype of the column
col_desc = filedata_.winery.describe()

# See the mean of a column
# Works only on int data types
col_mean = filedata_.points.mean()

# See the list of unique values in a column
col_unique = filedata_.points.unique()

# See the list of unique values and how often they occur in the dataset
col_value = filedata_.points.value_counts()

# map() is the first, and slightly simpler one. For example, suppose that 
# we wanted to remean the scores the wines received to 0. We can do this as follows:
col_map = filedata_.points.map(lambda p: p - col_mean)

# Pandas provides many common mapping operations as built-ins. 
# For example, here's a faster way of remeaning our points column:
col_mean_apply = filedata_.points - col_mean

# apply() is the equivalent method if we want to transform a whole DataFrame by 
# calling a custom method on each row.
def remean_points(row):
    row.points = row.points - col_mean
    return row

# The apply object always takes a function as an argument
filedata_.apply(remean_points, axis='columns')

# Return the row label of the maximum value.
# If multiple values equal the maximum, the first row label with that value is returned.
bargain_idx = (filedata_.points / filedata_.price).idxmax()

# Use a map to check each description for the string tropical, then count up the number of times this is True. 
# Repeat this for fruity. Finally, create a Series combining the two values.
n_trop = filedata_.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = filedata_.description.map(lambda desc: "fruity" in desc).sum()
desc_count = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])


#7.We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too 
# hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts 
# as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star. 
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should 
# automatically get 3 stars, regardless of points. Create a series star_ratings with the number of stars 
# corresponding to each review in the dataset.
def make_stars(set): 
        if set.country == 'Canada':
             return 3
        elif set.points >= 95:
            return 3
        elif set.points >= 85:
            return 2
        else:
            return 1

create_stars = filedata_.apply(make_stars, axis=1)

print(create_stars)