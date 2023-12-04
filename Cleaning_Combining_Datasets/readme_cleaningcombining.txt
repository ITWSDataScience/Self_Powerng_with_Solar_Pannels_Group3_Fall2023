Scripts for the cleaning and combining of data for Data Science, Fall 2023, Group 3. Written by Cooper Hay.

All scripts are written with the intention of taking Aashi's cleaned data output ('Solar_Project.csv') and
combining it with additional datasets to help derive further meaning. 

get_fips.py and adding_fips.py clean the dataset that contains the FIPS code associated with each county and then
adds the FIPS code associated with each county name. This enables the inclusion of datasets that have county-based
data using FIPS code instead of the name of each county (any FIPS code in the United States is unique to one county).
Output: Solar Project data from Aashi with each county's associated FIPS code.

add_unemployment.py adds unemployment and income data to the dataset generated above. Using the FIPS code, the associated
2022 unemployment rate, 2021 median household income, and the percentage of the NY state median income are all added.
Estimated production and PV system size from the Solar_Project dataset are aggregated by county. The output data contains 
data for unemployment, income, and solar production for each county in the state of New York. 

Due to a lack of data points, the dataset created using the above scripts was not used for any modeling. However, its 
inclusion reflects some of the preliminary EDA that took place but was not included in our final report.

To give our models more data points, we pivoted from using data by county to using data by zip code. This would 
give us around 1,500 data points to use with our models. To accompany this, a dataset with NY income by county was 
retrieved from the United States Census Bureau. 

zip_code_income.py pulls mean annual income by zip code in NY. This data is then combined with Aashi's 'Solar_Project.csv'
in get_prod_by_zip.py to combine production data and income data. The resulting dataset has aggregate solar system size and 
production by zip code along with mean income by zip.
