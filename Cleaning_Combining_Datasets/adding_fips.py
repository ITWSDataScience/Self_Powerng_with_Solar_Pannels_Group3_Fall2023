import pandas as pd

fips = pd.read_csv('county_fips.csv',index_col=None)

data = pd.read_csv('Solar_Project.csv')

def get_fips(county):
    #print(county)
    result = fips.loc[fips['County_Name'] == county, 'County_FIPS'].tolist()
    #print(result[0])
    return result[0]

data['County_FIPS'] = data['County'].apply(get_fips)
data.to_csv('Solar_Project_FIPS.csv',index=False)
