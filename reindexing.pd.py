import pandas as pd
import numpy as np

columns = ['a', 'b', 'c', 'd', 'e']
index = ['A', 'B', 'C', 'D', 'E']

# Create a DataFrame of random values of array
df1 = pd.DataFrame(np.random.rand(5, 5), columns=columns, index=index)

print(df1)

print('\n\ndataframe after reindexing rows: \n',
      df1.reindex(['B', 'A', 'D', 'C', 'E']))

                   