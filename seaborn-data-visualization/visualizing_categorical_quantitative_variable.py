# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
survey_data = pd.read_csv('survey_data.csv')
# Change the orientation of the plot
sns.catplot(x="Internet usage", data=survey_data,
            kind="count",col="Age Category")

# Show plot
plt.show()

# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender",y="Interested in Math", data=survey_data,
            kind="bar")


# Show plot
plt.show()

# Load another dataset
student_data = pd.read_csv('student_data.csv')

# Create bar plot of average final grade in each study category
sns.catplot(x="study_time",y="G3", data=student_data,kind="bar")

# Show plot
plt.show()


# List of categories from lowest to highest
category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci=None
            )

# Show plot
plt.show()

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time",y="G3", data=student_data,
            kind="box",
            order=study_time_order
            )


# Show plot
plt.show()

# Create a box plot with subgroups and omit the outliers
sns.catplot(
    x="internet",
    y="G3",
    data=student_data,
    kind="box",
    hue="location",
    fliersize=0,
    sym=""
)

# Show plot
plt.show()

# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()

# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point")

# Show plot
plt.show()


# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,
           join=False)
# Show plot
plt.show()

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school")

# Show plot
plt.show()

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()


