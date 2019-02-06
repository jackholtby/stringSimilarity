import pandas
from difflib import SequenceMatcher

def similar(first, second):
    return SequenceMatcher(None, first, second).ratio()

testTable = pandas.read_csv('test.csv', index_col='test_id')


for row in testTable.itertuples():
