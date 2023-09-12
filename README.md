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

