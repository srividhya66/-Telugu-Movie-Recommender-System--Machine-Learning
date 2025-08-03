import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    movies = pd.read_csv("telugu_movies.csv")
    movies.columns = movies.columns.str.strip()
    movies.rename(columns={'Title': 'title', 'Genre': 'overview'}, inplace=True)
    movies = movies[['title', 'overview']].dropna()
    return movies

def create_similarity_matrix(movies):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['overview'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

def recommend(title, movies, similarity):
    index = movies[movies['title'].str.lower() == title.lower()].index
    if len(index) == 0:
        return ["Movie not found."]
    
    index = index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)
    recommended = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended
