# AIML Lab Programs (2026)

Python implementations for the exercises in the BCS501G Artificial Intelligence and Machine Learning lab manual (2026).
Each script begins with its corresponding question. The implementations are cleaned up for current Python and use self-contained or built-in datasets where practical.

## Programs

| Exercise | Program | Question |
|---|---|---|
| 1a | [01a_chatbot.py](01a_chatbot.py) | Demonstrate a simple chatbot with at least 10 conversations. |
| 1b | [01b_tic_tac_toe.py](01b_tic_tac_toe.py) | Implement a Tic-Tac-Toe game. |
| 2a | [02a_a_star.py](02a_a_star.py) | Implement the A* algorithm. |
| 2b | [02b_ao_star.py](02b_ao_star.py) | Implement the AO* algorithm. |
| 3 | [03_em_vs_kmeans.py](03_em_vs_kmeans.py) | Apply EM and k-Means to a dataset, compare clustering results, and comment on quality. |
| 4 | [04_knn_iris.py](04_knn_iris.py) | Classify the Iris dataset with KNN and print a confusion matrix. |
| 5 | [05_linear_regression.py](05_linear_regression.py) | Demonstrate linear regression on a suitable dataset and predict an output. |
| 6 | [06_id3_decision_tree.py](06_id3_decision_tree.py) | Build an ID3 decision tree and classify a new sample. |
| 7 | [07_naive_bayes.py](07_naive_bayes.py) | Implement Naive Bayes for classification. |
| 8 | [08_gibbs_sampling.py](08_gibbs_sampling.py) | Demonstrate Gibbs sampling and generate posterior samples. |
| 9 | [09_backpropagation_ann.py](09_backpropagation_ann.py) | Implement backpropagation and test an artificial neural network. |
| 10 | [10_svm_classifier.py](10_svm_classifier.py) | Demonstrate an SVM classifier on a suitable dataset. |

## Setup

Python 3.10 or newer is recommended.

```bash
python -m pip install -r requirements.txt
```

Run a program from this directory, for example:

```bash
python 04_knn_iris.py
```

Programs that draw charts may open a Matplotlib window. The original manual refers to local CSV files for some exercises; these versions use scikit-learn's included datasets or a small in-file dataset so they can run without those machine-specific paths.
