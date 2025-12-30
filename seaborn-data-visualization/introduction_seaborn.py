# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
gdp = [1000, 2000, 3000, 4000, 5000]
percent_literate = [60, 70, 80, 90, 95]
region = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

# Import pandas
import pandas as pd

# Define csv file path
csv_filepath = '../data/mpg.csv'

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())


# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
student_data = pd.read_csv('../data/student.csv')
sns.scatterplot(x="absences", y="G3",
                data=student_data,
                hue="location",
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(
    x="school",
    data=student_data,
    hue="location",
    palette=palette_colors
)


# Display plot
plt.show()