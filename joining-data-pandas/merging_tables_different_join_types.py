# Import pandas as pd
import pandas as pd
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import the movies and financials DataFrames
movies = pd.read_csv('../data/movies.csv')
financials = pd.read_csv('../data/financials.csv')

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Load the toy_story and taglines DataFrames
toy_story = pd.read_csv('../data/toy_story.csv')
taglines = pd.read_csv('../data/taglines.csv')

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how='inner')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Load the movies, scifi_movies, and action_movies DataFrames
movies = pd.read_csv('../data/movies.csv')
scifi_movies = pd.read_csv('../data/scifi_movies.csv')
action_movies = pd.read_csv('../data/action_movies.csv')

# Merge scifi_movies and action_movies on id using a right join
scifi_action = scifi_movies.merge(action_movies, on='movie_id', how='right')

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isna()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id', how='inner')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

# Load the pop_movies and movie_to_genres DataFrames
pop_movies = pd.read_csv('../data/pop_movies.csv')
movie_to_genres = pd.read_csv('../data/movie_to_genres.csv')

print(pop_movies.head())
print(movie_to_genres.head())

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', left_on='movie_id', right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

# Load the iron_1_actors and iron_2_actors DataFrames
iron_1_actors = pd.read_csv('../data/iron_1_actors.csv')
iron_2_actors = pd.read_csv('../data/iron_2_actors.csv')

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on='id',
                                     how='outer',
                                     suffixes=('_1', '_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isna()) |
     (iron_1_and_2['name_2'].isna()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())

# Load the crews DataFrame
crews = pd.read_csv('../data/crews.csv')

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',suffixes=('_dir', '_crew'))

# Load the movies and ratings DataFrames
ratings = pd.read_csv('../data/ratings.csv')

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Load the sequels and financials DataFrames
sequels = pd.read_csv('../data/sequels.csv', index_col='id')
financials = pd.read_csv('../data/financials.csv', index_col='id')

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, left_index=True, right_index=True, how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, left_on='sequel', right_index=True,
                              how='inner', suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff',ascending=False).head())
