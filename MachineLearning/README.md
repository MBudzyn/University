# 🤖 Machine Learning

This repository contains materials, lab notebooks, and lecture implementations from the **Machine Learning** course at the **University of Wrocław**.  
It covers both the **theoretical foundations** and **practical implementations** of the most important classical machine learning algorithms.

---

## 🧭 Overview

The course focuses on understanding **core machine learning concepts** — from data preprocessing and model training, to evaluation and visualization.  
The repository is divided into:

- **`lectures/`** — Core algorithm implementations in Python (manual, from scratch)
- **`lab_sessions/`** — Practical exercises and Jupyter notebooks
- **`extra_exercises/`** — Additional assignments, experiments, and exploratory tasks
- **`theory/`** — Supplementary notes and visual summaries

---

## 🧩 Topics Covered

- 📊 **Data Preprocessing** — Cleaning, encoding, filling missing values, normalization  
- 🧠 **Supervised Learning Algorithms**
  - *k*-Nearest Neighbors (KNN)
  - Linear & Logistic Regression
  - Stochastic Gradient Descent (SGD)
  - Decision Trees & Ensemble methods
  - k-Means / k-Centers Clustering  
- 🧮 **Feature Engineering** — Encoding categorical variables, feature scaling, PCA  
- 📈 **Model Evaluation** — Train/test split, cross-validation, metrics (accuracy, precision, recall, etc.)  
- 🧰 **Visualization & Interpretation** — Exploratory plots and performance graphs  

---

## 🗂️ Folder Structure

```bash
MachineLearning/
├─ lectures/                     # Core ML algorithm implementations
│   └─ lecture1/                 
│       ├─ knn.py
│       ├─ linear_regression.py
│       ├─ logistic_regression.py
│       └─ sgd.py
│
├─ lab_sessions/                 # Practical lab assignments
│   ├─ list1/ ... list4/         # Each folder = one lab task set
│   └─ *.ipynb                   # Notebooks with analysis and experiments
│
├─ extra_exercises/              # Additional explorations and extended projects
│   ├─ additional1/ ...          # Topic-based folders (feature engineering, time series, etc.)
│   ├─ models.py
│   └─ plot_fun.py
│
└─ theory/                       # Notes
    └─ cv note.png
