import pandas as pd
import datetime as dt
import numpy as np

start_date = dt.datetime(2023, 1, 1, 8, 30, 0)
end_date = dt.datetime(2023, 2, 1, 10, 45, 0)

df = pd.DataFrame(index=pd.date_range(start=start_date, end=end_date, freq='H')).reset_index().rename(columns={'index': 'datetime'})

print("Sample datetime data:")
print(df.head(10))

df['ts'] = df['datetime'].values.astype(np.int64) // 10 ** 9
print("\nConvert datetime to timestamp:")
print(df[['datetime', 'ts']].head(10))


