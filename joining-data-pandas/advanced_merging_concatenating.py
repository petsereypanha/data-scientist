# Import pandas as pd
import pandas as pd
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Load the top_cust and employees DataFrames
top_cust = pd.read_csv('../data/top_cust.csv')
employees = pd.read_csv('../data/employees.csv')

# Merge employees and top_cust
empl_cust = employees.merge( top_cust, on='srid',
                            how='left' , indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

# Load the non_mus_tcks, top_invoices, and genres DataFrames
non_mus_tcks = pd.read_csv('../data/non_mus_tcks.csv')
top_invoices = pd.read_csv('../data/top_invoices.csv')
genres = pd.read_csv('../data/genres.csv')

# Merge non_mus_tcks and top_invoices on 'tid' using an inner join
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid', how='inner')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid': 'count'})

# Merge cnt_by_gid with genres on gid and print the result
result = cnt_by_gid.merge(genres, on='gid')
print(result)

# Load the tracks DataFrames
tracks_master = pd.read_csv('../data/tracks_master.csv')
tracks_ride = pd.read_csv('../data/tracks_ride.csv')
tracks_st = pd.read_csv('../data/tracks_st.csv')

# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1

tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],ignore_index=True, sort=True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],join='inner',sort=True)
print(tracks_from_albums)

# Import the pandas libraries
import pandas as pd
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Load the invoice DataFrames
inv_jul = pd.read_csv('../data/inv_jul.csv')
inv_aug = pd.read_csv('../data/inv_aug.csv')
inv_sep = pd.read_csv('../data/inv_sep.csv')

# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                            keys=['7Jul', '8Aug', '9Sep'],
                            names=['Month', 'Invoice'])

avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

avg_inv_by_month.plot(kind='bar', title='Average Invoice Total by Month')
plt.show()

# Load the classic_18, classic_19,pop_18 and pop_19  DataFrames
classic_18 = pd.read_csv('../data/classic_18.csv')
classic_19 = pd.read_csv('../data/classic_19.csv')
pop_18 = pd.read_csv('../data/pop_18.csv')
pop_19 = pd.read_csv('../data/pop_19.csv')

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid', how='inner')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)