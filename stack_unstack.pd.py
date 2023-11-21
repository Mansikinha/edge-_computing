import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Apple': [10, 15, 20],
    'Banana': [5, 8, 12],
    'Cherry': [3, 6, 9]
}

df = pd.DataFrame(data)

stacked_df = df.set_index('Date').stack().reset_index(level=1, name='Value').reset_index()

print("Stacked DataFrame:")
print(stacked_df)

unstacked_df = df.set_index(['Date']).stack().unstack().reset_index()

print("\nUnstacked DataFrame:")
print(unstacked_df)
