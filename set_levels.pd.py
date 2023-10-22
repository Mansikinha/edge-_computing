import pandas as pd

# Create arrays
employees = [
        ['E101', 'E102', 'E102', 'E103'],
        ['AV', 'Al', 'DN', 'JY']
    ]

# create a Multiindex using  from_arrays() 
mi = pd.MultiIndex.from_arrays(employees, names=('emp_ids', 'names'))

# display the Multiindex
print("The MultiIndex...\n",mi)
print()

# Get the levels in MultiIndex
print("The levels in MultiIndex...\n",mi.levels)
print()

# set the levels in MultiIndex
print("Setting new levels...\n",
    mi.set_levels([['e111', 'e112', 'e113', 'e114'], 
    ['AG', 'EM', 'KT', 'GA']]))
