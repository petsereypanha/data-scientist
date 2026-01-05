# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load the Spotify dataset
spotify_data = pd.read_csv('spotify_data.csv')
# Take a random sample of 1000 songs from the dataset
spotify_sample = spotify_data.sample(n=1000, random_state=42)

# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(n=len(spotify_sample), replace=True)

# Print the resample
print(spotify_1_resample)

# Calculate of the danceability column of spotify_1_resample
mean_danceability_1 = spotify_1_resample['danceability'].mean()

# Print the result
print(mean_danceability_1)

# Replicate this 1000 times
mean_danceability_1000 = []
for _ in range(1000):
    mean_danceability_1000.append(
        np.mean(spotify_sample.sample(frac=1, replace=True)['danceability'])
    )

# Print the result
print(mean_danceability_1000)

# Replicate this 1000 times
mean_danceability_1000 = []
for i in range(1000):
	mean_danceability_1000.append(
        np.mean(spotify_sample.sample(frac=1, replace=True)['danceability'])
	)

# Draw a histogram of the resample means
plt.hist(mean_danceability_1000)
plt.show()

mean_popularity_2000_samp = []
# Define the population as the entire spotify_data
spotify_population = spotify_data

# Generate a sampling distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_samp.append(
    	# Sample 500 rows and calculate the mean popularity
        spotify_population.sample(n=500, replace=False)['popularity'].mean()
    )

# Print the sampling distribution results
print(mean_popularity_2000_samp)

mean_popularity_2000_boot = []

# Generate a bootstrap distribution of 2000 replicates
for i in range(2000):
    mean_popularity_2000_boot.append(
    	# Resample 500 rows and calculate the mean popularity
    	spotify_sample.sample(n=500, replace=True)['popularity'].mean()
    )

# Print the bootstrap distribution results
print(mean_popularity_2000_boot)

# Store the sampling distribution and bootstrap distribution in variables
sampling_distribution = mean_popularity_2000_samp
bootstrap_distribution = mean_popularity_2000_boot

# Calculate the population mean popularity
pop_mean = spotify_population['popularity'].mean()

# Calculate the original sample mean popularity
samp_mean = spotify_sample['popularity'].mean()

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)

# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])

# Calculate the population std dev popularity
pop_sd = spotify_population["popularity"].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample["popularity"].std(ddof=1)

# Calculate the sampling dist'n estimate of std dev popularity
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)

# Calculate the bootstrap dist'n estimate of std dev popularity
boot_distn_sd = np.std(bootstrap_distribution, ddof=1) * np.sqrt(5000)

# Print the standard deviations
print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])

# Generate a 95% confidence interval using the quantile method
lower_quant = np.percentile(bootstrap_distribution, 2.5)
upper_quant = np.percentile(bootstrap_distribution, 97.5)

# Print quantile method confidence interval
print((lower_quant, upper_quant))


# Find the mean and std dev of the bootstrap distribution
point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution, ddof=1)

# Find the lower limit of the confidence interval
lower_se = norm.ppf(0.025, loc=point_estimate, scale=standard_error)

# Find the upper limit of the confidence interval
upper_se = norm.ppf(0.975, loc=point_estimate, scale=standard_error)

# Print standard error method confidence interval
print((lower_se, upper_se))