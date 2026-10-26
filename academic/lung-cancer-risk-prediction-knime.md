# Predicting lung cancer risk level with decision trees, KNN and Naive Bayes

*Graduate machine learning course, final project (MSc, Computer Engineering, May 2023). Individual project built in KNIME on a public dataset. This is a classroom study, not a medical tool.*

## Goal

Compare three classic classifiers on a public dataset and see how well they predict a patient's risk level (low, medium, high) from lifestyle, environment and symptom features.

## Data

- Public dataset from Kaggle: patients and air pollution, 1,000 rows, 23 input features and a three-level risk label.
- Features include age, gender, air pollution exposure, smoking, alcohol use, occupational hazards, genetic risk, chronic lung disease, diet, obesity and a set of symptoms.
- The dataset is public, anonymized and shared by a dataset platform for research and learning. It was used for academic purposes only; no personal or clinical records were collected or used.

## Method

1. Load the file and drop columns that are not features.
2. Split into training and test sets.
3. Train and test three models in KNIME:
   - **Decision tree**, using both the Gini index and gain ratio as split criteria.
   - **K-nearest neighbours**, with 3 and with 7 neighbours.
   - **Naive Bayes**.
4. Compare accuracy and read the confusion output for each model.

## Results

| Model | Accuracy |
|---|---|
| Decision tree (Gini and gain ratio) | 100% |
| KNN, 3 neighbours | 99.67% |
| KNN, 7 neighbours | 94.33% |
| Naive Bayes | 86.97% |

## How to read the results

Note: the original 2023 report treated the 100% as the best result. The points below are my review of it now.

- Decision trees and KNN fit this dataset very well; Naive Bayes was lower, which fits its assumption that features are independent while many of these features are strongly related.
- A perfect score on a small public dataset is a warning sign, not a success. It usually means the classes are cleanly separable in this data, and it says little about real patients.
- The study does not show that air pollution causes lung cancer, and it makes no clinical claim.

## What I would do next

- Use cross-validation instead of one split.
- Check for leakage between features and the label.
- Report precision, recall and a confusion matrix per class, not accuracy alone.
- Try a held-out dataset from a different source.

## What I took from it

- Good evaluation matters more than a high number.
- Simple, explainable models are a sensible first step; they are easy to explain to non-specialists.
- The same discipline (test, compare, state the limits) applies to any scoring or risk rule I build.
