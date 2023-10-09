import pandas as pd
import numpy as np

# Create a date range and generate random values
date_rng = pd.date_range(start='2023-01-01', end='2023-03-31', freq='D')
values = np.random.randint(0, 10, size=len(date_rng))

df = pd.DataFrame({'date_column': date_rng, 'value': values})

# Set 'date_column' as the index
df.set_index('date_column', inplace=True)

# Resample to monthly frequency and aggregate by sum
resampled_df = df.resample('M').sum()

print("Original DataFrame:")
print(df.head())
print("\nResampled DataFrame:")
print(resampled_df)
