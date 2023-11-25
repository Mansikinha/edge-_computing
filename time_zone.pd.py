import pandas as pd
print("Timezone: Europe/Berlin:")
print("Using pytz:")
date_pytz = pd.Timestamp('2023-01-01', tz = 'Europe/Berlin')
print(date_pytz.tz)  
print("Using dateutil:")
date_util = pd.Timestamp('2023-01-01', tz = 'dateutil/Europe/Berlin')
print(date_util.tz)
print("\nUS/Pacific:")
print("Using pytz:")
date_pytz = pd.Timestamp('2023-01-01', tz = 'US/Pacific')
print(date_pytz.tz)  
print("Using dateutil:")
date_util = pd.Timestamp('2023-01-01', tz = 'dateutil/US/Pacific')
print(date_util.tz)



