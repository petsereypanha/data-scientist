# import libraries
import pandas as pd
import pingouin as pg
from scipy.stats import shapiro
import warnings
warnings.filterwarnings('ignore')

def load_dataset(file_path):
    return pd.read_csv(file_path)
# load dataset  woman
women = load_dataset("../data/women_results.csv")

# load dataset man
men = pd.read_csv("../data/men_results.csv")

def check_dataframe(dataframe):
    print('_HEAD_'.center(50, '*'))
    print(dataframe.head(), '\n')
    print('_TAIL_'.center(50, '*'))
    print(dataframe.tail(), '\n')
    print('_SHAPE_'.center(50, '*'))
    print(dataframe.shape, '\n')
    print('_DATAFRAME INFO_'.center(50, '*'))
    print(dataframe.info(), '\n')
    print('_COLUMNS_'.center(50, '*'))
    print(dataframe.columns, '\n')
    print('_ANY NULL VALUE_'.center(50, '*'))
    print(dataframe.isna().values.any(), '\n')
    print('_TOTAL NULL VALUES_'.center(50, '*'))
    print(dataframe.isna().sum(), '\n')
    print('_DESCRIBING DATAFRAME_'.center(50, '*'))
    print(dataframe.describe([0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]).T)


check_dataframe(women)
check_dataframe(men)

# categorical columns
cat_col_women = [col for col in men.columns if men[col].dtypes == 'O']
cat_col_men = [col for col in men.columns if men[col].dtypes == 'O']

# removing "date" variable from categorical columns
cat_col_women = [col for col in cat_col_women if col not in 'date']
cat_col_men = [col for col in cat_col_men if col not in 'date']
print(cat_col_women, cat_col_men)

for col in cat_col_women:
    print(women[col].value_counts())

for col in cat_col_men:
    print(men[col].value_counts())

# Converting datetype of the variable "date" to datetime
women['date'] = pd.to_datetime(women['date'])
men['date'] = pd.to_datetime(men['date'])
print(women['date'].dtypes, men['date'].dtypes)

df_women = women.loc[(women['tournament'] == 'FIFA World Cup') & (women['date'] > '2002-01-01')]
df_men = men.loc[(men['tournament'] == 'FIFA World Cup') & (men['date'] > '2002-01-01')]
print(df_women.head(), '\n')
print(df_men.head())

df_women['goals_scored'] = df_women['home_score'] + df_women['away_score']
df_men['goals_scored'] = df_men['home_score'] + df_men['away_score']

df_women['goals_scored'].plot(kind='hist')
df_men['goals_scored'].plot(kind='hist')

# Calculation of mean goal scores for women and determination of normality
print(f"The mean of goals scored for women is {df_women['goals_scored'].mean()}.")
statistic, p_value = shapiro(df_women['goals_scored'])
print(f"Statistic: {statistic} and P value: {p_value}")

alpha = 0.01
if p_value > alpha:
    print("The data looks normally distributed (fail to reject H0)", '\n')
else:
    print("The data does not look normally distributed (reject H0)", '\n')

# Calculation of mean goal scores for men and determination of normality
print(f"The mean of goals scored for women is {df_men['goals_scored'].mean()}.")
statistic, p_value = shapiro(df_men['goals_scored'])
print(f"Statistic: {statistic} and P value: {p_value}")


# using pingouin
result = pg.mwu(df_women['goals_scored'], df_men['goals_scored'], alternative="greater")
p_val = result['p-val'].values[0]

# Create the required result_dict
result_dict = {
    "p_val": p_val,
    "result": "reject" if p_val < alpha else "fail to reject"
}