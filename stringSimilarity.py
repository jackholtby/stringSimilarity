import pandas
from difflib import SequenceMatcher

def similar(first, second):
    return SequenceMatcher(None, first, second).ratio()

testTable = pandas.read_csv('test.csv', index_col='test_id')


for row in testTable.itertuples():
    desc_x = row[1]
    desc_y = row[2]
    print(desc_x, desc_y)
    print(similar(desc_x, desc_y))
#    print(similar(row[2], row[3]))
