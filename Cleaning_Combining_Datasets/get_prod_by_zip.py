import pandas as pd

zip_income = pd.read_csv('income_by_zip_ny.csv',index_col=None)

data = pd.read_csv('Solar_Project.csv')

zips_with_incomedata = set(zip_income['ZIP'].tolist())

zips_with_proddata = set(data['Zip'].tolist())

intersect = zips_with_incomedata.intersection(zips_with_proddata)

# Get zip codes for which we have production data and income data.

zips_use = list(intersect)


out_data = []
for zip in zips_use:

    zip_income_data = zip_income[zip_income['ZIP'] == zip]

    #zip_income_data = zip_income.loc[zip_income['ZIP'] == zip]
    zip_income_num = zip_income_data['Mean_Income'].item()

    zip_code_data = data.loc[data['Zip'] == zip]

    estimated_size_sum = round(zip_code_data['Estimated PV System Size (kWdc)'].sum(),3)
    pv_system_size_sum = round(zip_code_data['PV System Size (kWac)'].sum(),3)
    pv_production_sum =  round(zip_code_data['Estimated Annual PV Energy Production (kWh)'].sum(),3)
    out_zip_data = [zip,zip_income_num,estimated_size_sum,pv_system_size_sum,pv_production_sum]
    
    out_data.append(out_zip_data)
    

out_df = pd.DataFrame(out_data,columns = ['ZIP',
    'Mean_Income',
    "Estimated PV System Size (kWdc)",
    "PV System Size (kWac)",
    "Estimated Annual PV Energy Production (kWh)"],
    index=None,
)

out_df = out_df.sort_values(by='ZIP',ascending=True)
out_df.to_csv('Solar_Project_ZIP_Income.csv',index=False)