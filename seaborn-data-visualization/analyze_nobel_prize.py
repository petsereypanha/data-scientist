import pandas as pd
import numpy as np

nobel = pd.read_csv('data/nobel.csv')
top_gender = nobel['sex'].value_counts().idxmax()
top_country = nobel['birth_country'].value_counts().idxmax()

nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)

nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'

decade_data = nobel.groupby('decade')['usa_born_winner'].agg(['sum', 'count'])

decade_data['ratio'] = decade_data['sum'] / decade_data['count']

max_decade_usa = decade_data['ratio'].idxmax()


female_nobel = nobel[nobel['sex'] == 'Female']

female_counts = female_nobel.groupby(['decade', 'category']).size().reset_index(name='female_count')
total_counts = nobel.groupby(['decade', 'category']).size().reset_index(name='total_count')

decade_category_counts = pd.merge(female_counts, total_counts, on=['decade', 'category'], how='right').fillna(0)

decade_category_counts['proportion'] = decade_category_counts['female_count'] / decade_category_counts['total_count']

max_row = decade_category_counts.loc[decade_category_counts['proportion'].idxmax()]

max_female_dict = {
    int(max_row['decade']): max_row['category']
}

first_woman = female_nobel.sort_values('year').iloc[0]

first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

repeat_winners = nobel['full_name'].value_counts()

repeat_list = list(repeat_winners[repeat_winners >= 2].index)

print(f"top_gender: {top_gender}")
print(f"top_country: {top_country}")
print(f"max_decade_usa: {max_decade_usa}")
print(f"max_female_dict: {max_female_dict}")
print(f"first_woman_name: {first_woman_name}")
print(f"first_woman_category: {first_woman_category}")
print(f"repeat_list: {repeat_list}")