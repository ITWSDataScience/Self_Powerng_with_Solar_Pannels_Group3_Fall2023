import pandas as pd


income_data_zip = pd.read_csv('ACSST5Y2021.S1901-Data.csv',usecols=['NAME','S1901_C01_013E'])
income_data_zip = income_data_zip.drop(index=[0,1])
income_data_zip = income_data_zip.rename(columns={'NAME':'ZIP','S1901_C01_013E':'Mean_Income'})

def parse_zip(unparsed):
    split = unparsed.split(' ')
    zip = split[1]
    #print(zip)
    return zip

def check_incomedata(incomedata):
    #print (type(incomedata))
    try:
        incomedata = int(incomedata)
    except ValueError:
        pass
    else:
        return int(incomedata)

print(income_data_zip)

# Get ZIP code from area data
income_data_zip['ZIP'] = income_data_zip['ZIP'].apply(parse_zip)

#Remove null / NaN values from income data
# 1826 ZIP codes to 1705.

income_data_zip = income_data_zip.query('Mean_Income.str.isnumeric()')
income_data_zip.to_csv('income_by_zip_ny.csv',index=False)

