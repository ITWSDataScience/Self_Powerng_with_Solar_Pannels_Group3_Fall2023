import pandas as pd
import numpy as np

data = pd.read_csv("Solar_Project_FIPS.csv",index_col=None)

counties = set(data['County_FIPS'].tolist())
counties=list(counties)

unemployment_data = pd.read_excel('Unemployment.xlsx',sheet_name='UnemploymentMedianIncome',header=4)

NY_unemployment = unemployment_data[unemployment_data['FIPS_Code'].isin(counties)]

fips = pd.read_csv('county_fips.csv',index_col=None)
county_pop = pd.read_csv('County_Population.csv',index_col = None)

out_data = []

for county in counties:

    county_fips_data = fips.loc[fips['County_FIPS'] == county]
    county_name = county_fips_data['County_Name'].item()

    county_pop_data = county_pop.loc[county_pop['County']== county_name]
    county_population = county_pop_data['Population'].item()
    county_population = int(county_population.replace(',',''))
    
    county_data = data.loc[data['County_FIPS'] == county]
    county_unemployment_data = NY_unemployment.loc[NY_unemployment['FIPS_Code'] == county]
    
    unemployment_rate_2022 = county_unemployment_data['Unemployment_rate_2022'].item()
    median_household_income_2021 = county_unemployment_data['Median_Household_Income_2021'].item()
    median_hh_income_pct_of_state_total_2021 = county_unemployment_data['Med_HH_Income_Percent_of_State_Total_2021'].item()
    estimated_size_sum = round(county_data['Estimated PV System Size (kWdc)'].sum(),3)
    pv_system_size_sum = round(county_data['PV System Size (kWac)'].sum(),3)
    pv_production_sum =  round(county_data['Estimated Annual PV Energy Production (kWh)'].sum(),3)

    out_county_data = [county, county_name, county_population, estimated_size_sum,pv_system_size_sum, pv_production_sum,unemployment_rate_2022,median_household_income_2021,median_hh_income_pct_of_state_total_2021]
    out_data.append(out_county_data)


out_df = pd.DataFrame(out_data,columns =["County_FIPS",
        "County_Name",
        "County_Population",
        "Estimated PV System Size (kWdc)",
        "PV System Size (kWac)",
        "Estimated Annual PV Energy Production (kWh)",
        "Unemployment_rate_2022",
        "Median_Household_Income_2021",
        "Med_HH_Income_Percent_of_State_Total_2021"],
        index=None)

out_df = out_df.sort_values(by='County_FIPS',ascending=True)
out_df.to_csv('Solar_Project_FIPS_Unemployment.csv',index=False)