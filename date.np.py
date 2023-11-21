import numpy as np

# Get today's date
today = np.datetime64('today', 'D')

# Get yesterday's date
yesterday = today - np.timedelta64(1, 'D')

# Get tomorrow's date
tomorrow = today + np.timedelta64(1, 'D')

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
