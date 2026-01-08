# Import necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import t
import matplotlib.pyplot as plt
import pingouin as pg
import seaborn as sns

def load_dataset(file_path):

    return pd.read_feather(file_path)

# load dataset Stack Overflow
stack_overflow = load_dataset("../data/stack_overflow.feather")

# load dataset Late Shipments
late_shipments = load_dataset("../data/late_shipments.feather")

# load dataset US Democrat vote
sample_dem_data = load_dataset("../data/dem_votes_potus_12_16.feather")

# load dataset US Republican vote
us_republican_vote = load_dataset("../data/repub_votes_potus_08_12.feather")

xbar_no = 34.61917757969854
xbar_yes = 37.19934784795096
s_no = 24.36859567958611
s_yes = 24.96582379766487
n_no = 700
n_yes = 300

# Calculate the numerator of the test statistic
numerator = xbar_no - xbar_yes

# Calculate the denominator of the test statistic
denominator = np.sqrt((s_no**2 / n_no) + (s_yes**2 / n_yes))

# Calculate the test statistic
t_stat = numerator / denominator

# Print the final test statistic (as requested in the prompt)
print(t_stat)

# Calculate the degrees of freedom
degrees_of_freedom = n_no + n_yes - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat, degrees_of_freedom)

# Print the p_value
print(p_value)

# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Print sample_dem_data
print(sample_dem_data)

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Print xbar_diff
print(xbar_diff)

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Print s_diff
print(s_diff)

# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins=20)
plt.show()

# Conduct a t-test on diff
test_results = pg.ttest(
    x=sample_dem_data['diff'],
    y=0,
    alternative='two-sided'
)

# Print the test results
print(test_results)

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pg.ttest(
    x=sample_dem_data['dem_percent_12'],
    y=sample_dem_data['dem_percent_16'],
    paired=True,
    alternative='two-sided'
)

# Print the paired test results
print(paired_test_results)

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].mean()

# Print the grouped means
print(xbar_pack_by_mode)

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby('shipment_mode')['pack_price'].std()

# Print the grouped standard deviations
print(s_pack_by_mode)

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x="pack_price", y="shipment_mode", data=late_shipments)
plt.show()

# Run an ANOVA for pack_price across shipment_mode
anova_results = pg.anova(data=late_shipments, dv='pack_price', between='shipment_mode')

# Print anova_results
print(anova_results)

# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pg.pairwise_ttests(
    data=late_shipments,
    dv='pack_price',
    between='shipment_mode',
    padjust=None
)
# Print pairwise_results
print(pairwise_results)
