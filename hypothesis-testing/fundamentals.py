# import laibraries
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import norm

# load dataset
def load_dataset(file_path):

    return pd.read_feather(file_path)

# load dataset Stack Overflow
stack_overflow = load_dataset("../data/stack_overflow.feather")

# load dataset Late Shipments
late_shipments = load_dataset("../data/late_shipments.feather")

# load dataset US Democrat vote
us_democrat_vote = load_dataset("../data/dem_votes_potus_12_16.feather")

# load dataset US Republican vote
us_republican_vote = load_dataset("../data/repub_votes_potus_08_12.feather")

# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = (late_shipments["late"] == "Yes").mean()

# Print the results
print(late_prop_samp)

# Generate a bootstrap distribution of the proportion of late shipments
n_iterations = 10000
late_shipments_boot_distn = np.empty(n_iterations)

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)

# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Calculate the p-value
p_value = 1 - norm.cdf(z_score)

# Print the p-value
print(p_value)

# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))