Excited to share my Data Science projects completed during my internship at Outrix!
(Movie Recommender System.)


**
Note:

The full credits.csv and similarity.pkl files are not included due to large file size constraints.

**

Objective

Suggest movies similar to a selected movie using metadata features.

Understand which movie attributes influence recommendations.

Deploy an interactive web application for real-time movie recommendations.

Tools & Technologies Used

Python – Core programming language for data processing and model building.

Pandas & NumPy – Data manipulation and preprocessing.

Scikit-learn – Machine learning and similarity computation.

Techniques: CountVectorizer for text vectorization, Cosine Similarity for recommendations.

Streamlit – Web app framework for deploying the interactive recommendation system.

Pickle – To save preprocessed data and similarity matrices for faster loading.



Key Features

Data Preprocessing:

Combine important movie features into a single tags column.

Clean and vectorize text data for similarity analysis.

Similarity Computation:

Compute cosine similarity between movies to find the most similar ones.

Recommendation Function:

Returns top 5 movies similar to a selected movie.

Interactive Web App:

Users select a movie from a dropdown menu.

Streamlit app displays recommendations in real-time.

Pickle Files for Deployment:

movie_dict.pkl → Stores movie data.

similarity.pkl → Stores precomputed similarity matrix.
