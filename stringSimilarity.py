import pandas
from difflib import SequenceMatcher

# Function to generate a similarity metric between to strings
def similar(first, second):
    return SequenceMatcher(None, first, second).ratio()

# Create pandas DataFrame from the test.csv file.
# Set test_id as the index.
testTable = pandas.read_csv('test.csv', index_col='test_id')

# Add new column (I'm hoping you meant this column)
# which has the metric of similarity stored in it.
testTable['same_security'] = similar(testTable['description_x'], testTable['description_y'])
