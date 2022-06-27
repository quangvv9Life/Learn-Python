# There are several ways to create a DataFrame. One way way is to use a dictionary.

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# Another way to create a DataFrame is by importing a csv file using Pandas. 
# Now, the csv G:/tryPython/Python Test/LearnPython.Org/Ingredient.csv is stored and can be imported using pd.read_csv:

ingredient = pd.read_csv(r'G:/tryPython/Python Test/LearnPython.Org/Ingredient.csv')
print(ingredient)

# Indexing DataFrames

# In the example below, you can use square brackets to select one column of the cars DataFrame. 
# You can either use a single bracket or a double bracket. 
# The single bracket will output a Pandas Series, while a double bracket will output a Pandas DataFrame.

# Import pandas and Ingredient.csv
ingredients = pd.read_csv('G:/tryPython/Python Test/LearnPython.Org/Ingredient.csv', index_col = 0)

# Print out country column as Pandas Series
print(ingredients['Unit'])

# Print out country column as Pandas DataFrame
print(ingredients[['Unit']])

# Print out DataFrame with country and drives_right columns
print(ingredients[[ 'Unit', 'quantity']])

# Square brackets can also be used to access observations (rows) from a DataFrame. For example:

print(ingredients[0:10])

# You can also use loc and iloc to perform just about any data selection operation. 
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels. 
# iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

print(ingredients.iloc[3])
print(ingredients.loc[['Gạo tẻ', 'Đường trắng']])