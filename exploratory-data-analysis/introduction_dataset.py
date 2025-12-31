# Import libraries
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt

# Load the unemployment dataset from a CSV file
unemployment = pd.read_csv('../data/unemployment.csv')

# Print the first five rows of unemployment
print(unemployment.head())

# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())

# Count the values associated with each continent in unemployment
print(unemployment['continent'].value_counts())

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=unemployment, x='2021', binwidth=1)
plt.show()

# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype(float)
# Print the dtypes to check your work
print(unemployment.dtypes)

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])

# Print the minimum and maximum unemployment rates during 2021
print(unemployment["2021"].min(), unemployment["2021"].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data=unemployment, x='2021', y='continent')
plt.show()

# Print the mean and standard deviation of rates for 2019 and 2020
print(unemployment[["2019", "2020"]].agg(['mean', 'std']))

# Print mean and standard deviation grouped by continent
print(unemployment[["continent", "2019", "2020"]].groupby("continent").agg(['mean', 'std']))

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=("2021", "mean"),
    # Create the std_rate_2021 column
    std_rate_2021=("2021", "std")
)
print(continent_summary)

# Create a bar plot of continents and their average unemployment
sns.barplot(data=unemployment, x="continent", y="2021")
plt.show()

