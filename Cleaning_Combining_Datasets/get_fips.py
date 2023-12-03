import pandas as pd

fips = pd.read_csv('NY_County_FIPS.csv',low_memory=False)

drop = ['City Name','Town Name','Village Name','Municipality']
fips.drop(drop,inplace=True,axis=1)

result = fips.drop_duplicates()
sorted = result.sort_values(by='County FIPS')
sorted.columns = [column.replace(' ', '_') for column in sorted.columns]
print(result)

sorted.to_csv('county_fips.csv',index=False)