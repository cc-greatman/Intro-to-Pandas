import pandas as pd
import IPython.display as display
import xlsxwriter
# Creating a Dataframe
df = pd.DataFrame({'Yes':[50,21], 'No':[100,42]},
                  index=['Have a Car', 'Have a Bath'])

# Converting DataFrames to CSV
make_ = df.to_csv("drone.csv")

# Series as a dataframe. Usually a single list of data
s = pd.Series(["happy A lot", 1, "합시다", "Food"], 
              index=['Flour', 'Eggs', 'Milk', 'Goat'], 
              name='Food Test')

print(df)
print(s)

