# Name: String Similarity
# Author: Jack Holtby
# Purpose: To load data from test.csv into pandas dataframe,
# calculate similarity between description_x and description_y
# and add this in a new column in the dataframe: same_security

import pandas
from difflib import SequenceMatcher

# Function to generate a similarity metric between to strings
def similar(first, second):
    return SequenceMatcher(None, first, second).ratio()

# Create pandas DataFrame from the test.csv file.
# Set test_id as the index.
testTable = pandas.read_csv('test.csv', index_col='test_id')

# List variable to store all the similarities
same_sec_list = []

# Store calculated similarities for each row in a list variable
for row in testTable.itertuples(index=True, name='test_id'):
    same_sec_list.append(similar(row[1], row[2]))

# Fill the same_security column (I hope that's what you meant)
# with the values from the list just generated.
testTable['same_security'] = same_sec_list

print(testTable)
