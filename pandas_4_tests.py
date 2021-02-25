# pandas_4 test cases

import pandas as pd
import pandas_4

# Test case 1 - ensure format of output is correct
d = {'month-yr': ['Sep-2017', 'Aug-2019'], 'Timestamp': [3, 2]}
df = pd.DataFrame(data=d, index=d['Timestamp'])
df.columns = ['month-yr', 'Timestamp']
index = df.index
index.name = 'Timestamp'
y = pandas_4.fix_categorical(df)
assert isinstance(y, pd.DataFrame), "y must be a pandas DataFrame"
assert 'month-yr' in y, "y must contain the month-yr column"
assert 'Timestamp' in y, "y must contain the Timestamp column (so that we can run the command 'x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()')"
assert y['month-yr'].dtype.name == 'category', "y['month-yr'] must be a PandasCategoricalDType order"

# Test case 2 - test ordering on smaller dataset. This tests that given a list of out-of-order dates (with multiple instances of some dates), 
# fix_categorical puts them in the correct chronological order
d = {'month-yr': ['Sep-2017', 'Aug-2019', 'Apr-2019', 'Apr-2011', 'Apr-2011', 'Aug-2019', 'Aug-2019'], 'Timestamp': [2, 4, 3, 0, 1, 5, 6]}
df = pd.DataFrame(data=d, index=d['Timestamp'])
df.columns = ['month-yr', 'Timestamp']
index = df.index
index.name = 'Timestamp'
y = pandas_4.fix_categorical(df)
assert y['month-yr'].values.tolist() == ['Apr-2011', 'Apr-2011', 'Sep-2017', 'Apr-2019', 'Aug-2019', 'Aug-2019', 'Aug-2019']

# Test case 3 - test ordering on larger dataset.
d = {'month-yr': ['Sep-2017', 'Aug-2019', 'Oct-2017', 'Jan-2017', 'Mar-2017', 'Feb-2017', 'Jan-2017', 'Jan-2018', 'May-2017', 'Jul-2017', 'Jun-2017', \
    'Apr-2019', 'Apr-2011', 'Apr-2011', 'Aug-2019', 'Dec-2017', 'Aug-2019', 'Sep-2017', 'Nov-2017'], 'Timestamp': [10, 16, 11, 2, 5, 4, 3, 14, 6, 8, 7, \
        15, 0, 1, 17, 13, 18, 9, 12]}
df = pd.DataFrame(data=d, index=d['Timestamp'])
df.columns = ['month-yr', 'Timestamp']
index = df.index
index.name = 'Timestamp'
y = pandas_4.fix_categorical(df)
assert y['month-yr'].values.tolist() == ['Apr-2011', 'Apr-2011', 'Jan-2017', 'Jan-2017', 'Feb-2017', 'Mar-2017', 'May-2017', 'Jun-2017', 'Jul-2017', 'Sep-2017', \
    'Sep-2017', 'Oct-2017', 'Nov-2017', 'Dec-2017', 'Jan-2018', 'Apr-2019', 'Aug-2019', 'Aug-2019', 'Aug-2019']

# Test case 4 - check that command 'x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index()' produces expected output
d = {'month-yr': ['Sep-2017', 'Aug-2019', 'Sep-2017', 'Apr-2011', 'Apr-2011', 'Apr-2011', 'Apr-2011', 'Jan-2018', 'Apr-2011', 'Apr-2011', 'Apr-2011', \
    'Apr-2019', 'Apr-2011', 'Apr-2011', 'Aug-2019', 'Sep-2017', 'Aug-2019', 'Apr-2011', 'Sep-2017'], 'Timestamp': [10, 16, 11, 2, 5, 4, 3, 14, 6, 8, 7, \
        15, 0, 1, 17, 13, 18, 9, 12]}
df = pd.DataFrame(data=d, index=d['Timestamp'])
df.columns = ['month-yr', 'Timestamp']
index = df.index
index.name = 'Timestamp'
y = pandas_4.fix_categorical(df)
Counts = y.groupby('month-yr')['Timestamp'].count().to_frame().sort_index() 
assert Counts['Timestamp'].values.tolist() == [10, 4, 1, 1, 3]