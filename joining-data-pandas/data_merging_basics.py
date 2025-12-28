# Import pandas as pd
import pandas as pd
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Load the taxi_owners and taxi_veh DataFrames
taxi_owners = pd.read_csv('../data/taxi_owners.csv')
taxi_veh = pd.read_csv('../data/taxi_veh.csv')

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid')

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid',
                                 suffixes=('_own', '_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

# Load the wards and census DataFrames
wards = pd.read_csv('../data/wards.csv')
census = pd.read_csv('../data/census.csv')

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)

# Print the first few rows of the wards_altered table to view the change
wards_altered = wards.copy()
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)

# Print the first few rows of the census_altered table to view the change
census_altered = census.copy()
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge(census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)

# Merge the licenses and biz_owners table on account
licenses = pd.read_csv('../data/licenses.csv')
biz_owners = pd.read_csv('../data/biz_owners.csv')
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
licenses_owners = licenses.merge(biz_owners, on='account')
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in descending order
sorted_df = counted_df.sort_values(by='account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

# load the ridership and cal DataFrames
cal = pd.read_csv('../data/cal.csv')
stations = pd.read_csv('../data/stations.csv')
ridership = pd.read_csv('../data/ridership.csv')

# head of the DataFrames
print(stations.head())
print(cal.head())
print(ridership.head())

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal)

ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
                                .merge(stations.astype({'station_id': int}), on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == 'Weekday')
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# Load the zip_demo DataFrames
zip_demo = pd.read_csv('../data/zip_demo.csv')

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
	.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))

# Load the land_use DataFrame
land_use = pd.read_csv('../data/land_use.csv')

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'],
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(by=['vacant', 'account', 'pop_2010'],
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())

