# CSE508_Winter2023_A2_48

## Data Preprocessing and TF-IDF Matrix Generation

In this section, we describe the data preprocessing steps performed on the provided dataset and the generation of TF-IDF matrices. This process is essential for preparing the data for various natural language processing tasks.

### Data Preprocessing

#### Relevant Text Extraction

For each of the 1400 files in the dataset, we performed the following steps:

1. **Relevant Text Extraction:** We extracted the contents between the `<TITLE>...</TITLE>` and `<TEXT>...</TEXT>` tags, concatenated the two strings using a blank space, and discarded the rest of the text. The resulting string was saved back to the same file.

2. **Preprocessing Steps:**
- **Lowercasing:** We converted all text to lowercase.
- **Tokenization:** We tokenized the text using the NLTK library's `word_tokenize()` method.
- **Stopword Removal:** We removed common stopwords using NLTK's stopword corpus.
- **Punctuation Removal:** We removed punctuation marks from the text.

Before and after performing each of these operations, we printed the contents of sample files to illustrate the changes.

### TF-IDF Matrix Generation

We generated TF-IDF matrices for the documents in the dataset. The following TF weighting schemes were employed:

1. **Binary Weighting:** Binary representation of term frequency.
2. **Count Weighting:** Term frequency counts.
3. **Frequency Weighting:** Frequency normalized by document length.
4. **Log Normalized TF:** Logarithmically normalized term frequency.
5. **Double Normalized TF:** Double normalization of term frequency.

For each term, we maintained dictionaries containing the corresponding TF values for each document and calculated document frequencies (DF). These TF-IDF matrices provide a basis for various information retrieval tasks.

### Jaccard Index

We also calculated the Jaccard Index for documents based on their word sets. This index measures the similarity between documents and can be useful for document retrieval and clustering.

For queries, we preprocessed them similarly to the documents and calculated the Jaccard Index between each query and document. The top-10 results based on these similarity scores were printed for each query.

## Naive Bayes Classifier with TF-ICF

This section contains the implementation of a Naive Bayes classifier with the TF-ICF (term frequency-inverse category frequency) weighting scheme for classifying documents into predefined categories based on their content. The dataset used for this task consists of news articles categorized into topics such as sports, tech, business, etc.

### Dataset

You can download the dataset from [Kaggle](https://www.kaggle.com/competitions/learn-ai-bbc/data). The dataset is in CSV format with columns 'ArticleId', 'Text', and 'Category'. Preprocessing and classification tasks were performed as follows:

### Data Preprocessing

- Removed unnecessary columns.
- Cleaned the text by removing punctuation, stop words, and converting it to lowercase.
- Tokenized the text.
- Performed stemming to reduce words to their root form.
- Implemented the TF-ICF weighting scheme.

### Data Splitting

The BBC train dataset was split into training and testing sets using a 70:30 split ratio.

### Training the Naive Bayes Classifier with TF-ICF

- Calculated the probability of each category based on the frequency of documents in the training set belonging to that category.
- Calculated the probability of each feature given each category based on the TF-ICF values.
- Implemented the Naive Bayes classifier using these probabilities.

### Testing the Classifier

- Used the testing set to evaluate the performance of the classifier.
- Calculated accuracy, precision, recall, and F1 score.

### Improving the Classifier

Experimented with different preprocessing techniques and parameters to improve classifier performance, including different split ratios (e.g., 80-20, 60-40, 50-50).
Tried different types of features, such as n-grams and TF-IDF weights.
Evaluated classifier performance after each experiment.

### Conclusion

In conclusion, the implementation of the Naive Bayes classifier with TF-ICF weighting scheme achieved an accuracy score of 0.8098434. Several experiments were conducted to improve performance, with the TF-IDF vectorization method outperforming TF-ICF. This is because TF-IDF considers the importance of terms across the entire corpus, providing a more balanced weighting scheme. Additionally, using n-grams decreased accuracy, potentially due to an increase in feature dimensionality and sparsity.

For a more detailed report on the implementation and experiments, please refer to the report.



