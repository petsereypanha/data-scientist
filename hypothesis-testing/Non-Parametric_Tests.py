import pandas as pd
from scipy.stats import t
import matplotlib.pyplot as plt
import pingouin as pingouin
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

# Count the freight_cost_group values
counts = late_shipments['freight_cost_group'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 50).all())

# Count the late values
counts = late_shipments['late'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 10).all())

# Count the values of freight_cost_group grouped by vendor_inco_term
counts = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 5).all())

# Count shipment_mode values
counts = late_shipments['shipment_mode'].value_counts()

# Print the result
print(counts)

# Inspect whether the counts are big enough
print((counts >= 30).all())

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(
    sample_dem_data['dem_percent_12'],
    sample_dem_data['dem_percent_16'],
    paired=True,
    alternative='two-sided'
)
# Print paired t-test results
print(paired_test_results)

# Conduct a Wilcoxon test on dem_percent_12 and dem_percent_16
wilcoxon_test_results = pingouin.wilcoxon(
    sample_dem_data['dem_percent_12'],
    sample_dem_data['dem_percent_16'],
    alternative='two-sided'
)

# Print Wilcoxon test results
print(wilcoxon_test_results)

# Select the weight_kilograms and late columns
weight_vs_late = late_shipments[['weight_kilograms', 'late']]

# Convert weight_vs_late into wide format
weight_vs_late_wide = weight_vs_late.pivot(columns='late', values='weight_kilograms')


# Run a two-sided Wilcoxon-Mann-Whitney test on weight_kilograms vs. late
wmw_test = pingouin.mwu(x=weight_vs_late_wide['Yes'], y=weight_vs_late_wide['No'], alternative='two-sided')


# Print the test results
print(wmw_test)

# Run a Kruskal-Wallis test on weight_kilograms vs. shipment_mode
kw_test = pingouin.kruskal(
    data=late_shipments,
    dv='weight_kilograms',
    between='shipment_mode'
)

# Print the results
print(kw_test)