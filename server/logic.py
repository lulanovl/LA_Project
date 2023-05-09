import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import ast
from .local_data import category
from .data_matrix import places
from .functions import argsort
from .functions import cosine_similarity




def recommend_places(place_attributes, user_preferences, k=5, n_components = 10):
    vectorizer = TfidfVectorizer(analyzer=lambda x: x)

    tfidf_matrix = vectorizer.fit_transform(place_attributes.values())

    # svd
    svd = TruncatedSVD(n_components=n_components)
    svd.fit(tfidf_matrix)
    u = svd.transform(tfidf_matrix)
    sigma = svd.singular_values_


    user_pref_matrix = vectorizer.transform([user_preferences])
    user_pref_reduced = user_pref_matrix.dot(svd.components_.T)


    # compute cosine similarity between the user preferences and the place attributes
    cosine_similarities = cosine_similarity(user_pref_reduced, u.dot(np.diag(sigma))).flatten()


    indices = cosine_similarities.argsort()[::-1][:k]
    recommendations = [list(place_attributes.keys())[i] for i in indices]

    return recommendations



def matching_algo(user_likes):

    attributes = ['Food', 'Entertainment', 'Cultural & Historical', 'Outdoor Activities', 
                'Trips', 'Get Drunk', 'Student', 'Friends', 'Family', 'Couples', 'Tourists']


    list_of_strings = ast.literal_eval(user_likes)
    sorted_places = recommend_places(places, list_of_strings, k=10)
    output = []
    for place in sorted_places:
        if place in category:
            output.append(category[place])
    
    return output
