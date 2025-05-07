import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix.csv')

df = df.rename(columns={
    'movie_title': 'Movie Title',
    'genre': 'Genre',
    'release_year': 'Release Year',
    'rating': 'Average Rating',
    'review_count': 'Number of Reviews'
})

df['Average Rating'] = df.groupby('Movie Title')['Average Rating'].transform('mean')

fig, axs = plt.subplots(2, 3, figsize=(16, 10))
fig.tight_layout(pad=4)

sns.countplot(data=df, x='Genre', order=df['Genre'].value_counts().index, ax=axs[0, 0])
axs[0, 0].set_title('Movies by Genre', fontsize=12)
axs[0, 0].set_xticklabels(axs[0, 0].get_xticklabels(), rotation=45, fontsize=10)
axs[0, 0].set_xlabel('')
axs[0, 0].set_ylabel('')

df['Popularity Index'] = df['Number of Reviews']
top_popular_movies = df[['Movie Title', 'Popularity Index']].sort_values(by='Popularity Index', ascending=False).head(10)
axs[0, 1].barh(top_popular_movies['Movie Title'], top_popular_movies['Popularity Index'])
axs[0, 1].set_title('Top Popular Movies', fontsize=12)
axs[0, 1].set_xlabel('')
axs[0, 1].set_ylabel('')

sns.boxplot(data=df, x='Genre', y='Average Rating', ax=axs[0, 2])
axs[0, 2].set_title('Genre vs Rating', fontsize=12)
axs[0, 2].set_xticklabels(axs[0, 2].get_xticklabels(), rotation=45, fontsize=10)
axs[0, 2].set_xlabel('')
axs[0, 2].set_ylabel('')

top_rated_movies = df[['Movie Title', 'Average Rating']].sort_values(by='Average Rating', ascending=False).head(10)
sns.barplot(data=top_rated_movies, x='Movie Title', y='Average Rating', ax=axs[1, 0])
axs[1, 0].set_title('Top 10 Movies Rated', fontsize=12)
axs[1, 0].set_xticklabels(axs[1, 0].get_xticklabels(), rotation=45, fontsize=10)
axs[1, 0].set_xlabel('')
axs[1, 0].set_ylabel('')

reviews_per_year = df.groupby('Release Year')['Number of Reviews'].sum().reset_index()
sns.lineplot(data=reviews_per_year, x='Release Year', y='Number of Reviews', marker='o', ax=axs[1, 1])
axs[1, 1].set_title('Reviews Over Time', fontsize=12)
axs[1, 1].set_xlabel('')
axs[1, 1].set_ylabel('')

# Remove any unused subplot axes
fig.delaxes(axs[1, 2])

plt.show()
