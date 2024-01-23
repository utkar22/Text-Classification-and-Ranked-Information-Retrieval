# Text Classification and Ranked Information Retrieval

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

## Ranked-Information Retrieval and Evaluation

In this section, we explore the task of Ranked-Information Retrieval and Evaluation using the Microsoft Learning to Rank dataset.

### Dataset

The dataset for this task can be accessed through the provided [link](https://www.microsoft.com/en-us/research/project/mslr/?from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fprojects%2Fmslr%2Fdownload.aspx%20). Specifically, we focus on queries with `qid:4`.

### Analysis

We rearranged query-url pairs based on relevance scores in reverse order to calculate the maximum Discounted Cumulative Gain (DCG). DCG is a measure of the effectiveness of a search algorithm in retrieving relevant documents, giving higher scores to more relevant documents that appear higher in the ranking. The number of possible arrangements was determined, resulting in a total of arrangements equal to \(59! \times 26! \times 17! \times 1!\). The calculated maximum DCG is 20.989750804831445.

The normalized Discounted Cumulative Gain (nDCG) was then calculated at position 50 and for the entire dataset. nDCG provides a normalized measure of the effectiveness of a search algorithm, taking into account the position of relevant documents in the ranking. For documents at position 50, nDCG is 0.3521042740324887, and for the entire dataset, nDCG is 0.5979226516897831.

Assuming a model that ranks URLs based on the value of feature 75 (sum of TF-IDF on the whole document), we plotted a Precision-Recall curve for the query `qid:4`. Precision and recall are metrics used to evaluate the performance of a search algorithm. Precision is defined as \(P(\text{relevant|retrieved})\), representing the proportion of retrieved documents that are relevant. Recall is defined as \(P(\text{retrieved|relevant})\), representing the proportion of relevant documents that are retrieved.

### Conclusion

This section concludes the exploration of Ranked-Information Retrieval and Evaluation, providing insights into DCG, nDCG, and a visual representation of the Precision-Recall trade-off for the specified query.




