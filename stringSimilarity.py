import pandas
from difflib import SequenceMatcher

testTable = pandas.read_csv('test.csv', index_col='test_id')

for row in testTable.itertuples():
