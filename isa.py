import pandas as pd

filepath_ = './Datasets/winemag-data_first150k.csv'
reviews = pd.read_csv(filepath_, index_col=0)

# Selecting a single column
desc = reviews.description

entire_col = reviews.iloc[:, 2]

# Also they are both row-first and column second

# selecting first row of data in a DF(returned as a series)
# more than on index, returns as a Dataframe
first_ = reviews.iloc[0]


# Displaying the first 10 variables of the chosen df
first_desc = reviews.iloc[:10, [1,0]]

## Label-based Selection
# Selecting the first 5 entry of two labels, country and winery
first_row = reviews.loc[:5, ['country', 'winery']]

## Conditional Selections
reviews.country == 'Italy'

# Selecting data with loc based on conditinals
italy = reviews.loc[reviews.country == 'Italy']

# Combining two questions togther
italy = reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

# Selecting records relevant to either question
fine = reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

## Using pandas in-built conditional selectors
countries = reviews.loc[reviews.country.isin(['Italy', 'France'])]
print(countries)