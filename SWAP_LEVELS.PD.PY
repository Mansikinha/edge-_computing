import pandas as pd

# Create arrays
employees = [
        ['E101', 'E102', 'E102', 'E103'],
       ['Al', 'AI', 'DL', 'JY'],
        [21, 19, 15, 17]
    ]

# create a Multiindex using  from_arrays() 
mi = pd.MultiIndex.from_arrays(employees, names=('emp_ids', 'names', 'age'))

# display the Multiindex
print("The MultiIndex...\n",mi)
print()

# Get the levels in MultiIndex
print("The levels in MultiIndex...\n",mi.levels)
print()

# Swap levels 0 and 1 of a MultiIndex
print("Swap levels...\n",mi.swaplevel(0,1))
print()

# Swap levels 0 and 2 of a MultiIndex
print("Swap levels...\n",mi.swaplevel(0,2))
print()

                                                 
