import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load the dataset
df = pd.read_csv('BBC News Train.csv')


# Split the data into training and testing sets
X = df['Text']
y = df['Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=89, test_size=0.2, shuffle=True)

# Implementing the TF-IDF weighting scheme
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)

# Training the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluating the model
X_test_tfidf = tfidf.transform(X_test)
y_pred = model.predict(X_test_tfidf)


print("Accuracy:", accuracy_score(y_test, y_pred))
