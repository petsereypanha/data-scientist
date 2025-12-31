# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()

crimes.columns = crimes.columns.str.replace(' ', '_')
crimes.columns = [col.lower() for col in crimes.columns]
crimes['hour_occ'] = crimes['time_occ'].str[:2].astype(int)
crimes.head()

sns.countplot(data=crimes, x='hour_occ')
plt.show()

# Fix: Get the hour with max crimes, not the count
peak_crime_hour = crimes['hour_occ'].value_counts().idxmax()
print(peak_crime_hour)

night_time = crimes[crimes["hour_occ"].isin([22,23,0,1,2,3])]
peak_night_crime_location = night_time.groupby("area_name", as_index=False)["hour_occ"].count().sort_values("hour_occ", ascending=False).iloc[0]["area_name"]
print(peak_night_crime_location)

crimes['age_bracket'] = pd.cut(crimes['vict_age'], bins=[0, 17, 25, 34, 44, 54, 64, np.inf], labels=["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"])
victim_ages = crimes['age_bracket'].value_counts()
print(victim_ages)