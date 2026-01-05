# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the employee attrition dataset
employee_population = pd.read_csv('data/employee_attrition.feather')
# Create a pandas Series from the Attrition column of employee_population
attrition_pop = employee_population['Attrition']
# Calculate the mean employee attrition in the population
mean_attrition_pop = employee_population['Attrition'].mean()

# Generate a simple random sample of 50 rows, with seed 2022
attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()

# Calculate the relative error percentage
rel_error_pct50 = (abs(mean_attrition_srs50 - mean_attrition_pop) / mean_attrition_pop) * 100

# Print rel_error_pct50
print(rel_error_pct50)

# Generate a simple random sample of 100 rows, with seed 2022
attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs100 = attrition_srs100['Attrition'].mean()

# Calculate the relative error percentage
rel_error_pct100 = (abs(mean_attrition_srs100 - mean_attrition_pop) / mean_attrition_pop) * 100

# Print rel_error_pct100
print(rel_error_pct100)

# Create an empty list
mean_attritions = []
# Loop 500 times to create 500 sample means
for i in range(500):
    mean_attritions.append(
    attrition_pop.sample(n=60)['Attrition'].mean()
    )

# Print out the first few entries of the list
print(mean_attritions[0:5])

# Create an empty list
mean_attritions = []
# Loop 500 times to create 500 sample means
for i in range(500):
	mean_attritions.append(
    	attrition_pop.sample(n=60)['Attrition'].mean()
	)

# Create a histogram of the 500 sample means
plt.hist(mean_attritions, bins=16, edgecolor='black')
plt.show()

# Function to expand a grid
def expand_grid(dicts):
    rows = 1
    for v in dicts.values():
        rows *= len(v)
    out = {k: np.repeat(v, rows // len(v)) for k, v in dicts.items()}
    for k, v in out.items():
        tile_size = rows // len(v)
        out[k] = np.tile(v, tile_size)
    return pd.DataFrame(out)

# Expand a grid representing five 8-sided dice
dice = expand_grid(
    {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
     'die2': [1, 2, 3, 4, 5, 6, 7, 8],
     'die3': [1, 2, 3, 4, 5, 6, 7, 8],
     'die4': [1, 2, 3, 4, 5, 6, 7, 8],
     'die5': [1, 2, 3, 4, 5, 6, 7, 8]
     })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = dice[['die1', 'die2', 'die3', 'die4', 'die5']].mean(axis=1)

dice['mean_roll'] = dice['mean_roll'].astype('category')

# Print result
print(dice)

# Expand a grid representing five 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] +
                     dice['die3'] + dice['die4'] +
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort=False).plot(kind='bar')
plt.show()

# Sample one to eight, five times, with replacement
five_rolls = np.random.choice(
    a=[1, 2, 3, 4, 5, 6, 7, 8],
    size=5,
    replace=True
)

# Print the mean of five_rolls
print(five_rolls.mean())

# Replicate the sampling code 1000 times
sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(
    np.random.choice(list(range(1, 9)), size=5, replace=True).mean()
    )

# Print the first 10 entries of the result
print(sample_means_1000[0:10])

# Replicate the sampling code 1000 times
sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(
  		np.random.choice(list(range(1, 9)), size=5, replace=True).mean()
    )

# Draw a histogram of sample_means_1000 with 20 bins
plt.hist(sample_means_1000, bins=20, edgecolor='black')
plt.show()

# Create empty lists to hold the sampling distributions
sampling_distribution_5 = []
sampling_distribution_50 = []
sampling_distribution_500 = []

# Calculate the mean of the mean attritions for each sampling distribution
sd_of_means_5 = np.std(sampling_distribution_5, ddof=1)
sd_of_means_50 = np.std(sampling_distribution_50, ddof=1)
sd_of_means_500 = np.std(sampling_distribution_500, ddof=1)

# Print the results
print(sd_of_means_5)
print(sd_of_means_50)
print(sd_of_means_500)
