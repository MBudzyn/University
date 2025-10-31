# 🧠 Time Series Gesture Recognition: A Comparative Study of Classic and Contrastive Learning  

A **comparative study** on gesture recognition from **multivariate time series data**, exploring the effectiveness of **classic machine learning algorithms** versus **Contrastive Learning (TF-C)**.  
Developed as part of academic coursework at the **University of Wrocław**.  

---

## 🎯 Project Overview  

The project focuses on recognizing **hand gestures** based on 3D accelerometer data.  
It compares traditional approaches — like **k-Nearest Neighbors** and **Random Forests** — against **TF-C**, a modern **Contrastive Learning** method for time series representation.  

### 🧩 Key Objectives  
- **Model Comparison:** Classic ML vs. Contrastive Learning (TF-C)  
- **Data Proficiency:** Effective preprocessing & visualization for time series data  
- **Benchmark Matching:** Reproducing results from the TF-C research paper  

---

## 👥 Team  

- Mateusz Budzyński  
- Maciej Ciepiela  
**Supervisor:** - Klaudia Blacer  

---

## 📓 Notebook Highlights – `gesture_prediction.ipynb`  

### 🔍 Data & Preprocessing  
- **Dataset:** UWaveGestureLibrary (.arff format)  
- **Input:** 3D accelerometer signals *(X, Y, Z)*  
- **Stratified split:** Train (240), Validation (80), Test (120)  
- **Visualizations:** Class distributions, statistical plots, 3D gesture trajectories  

### ⚙️ Feature Engineering  
- **Sliding Window:** Extracted mean, standard deviation, and median statistics  
- **Seasonal Decomposition:** Captured underlying trends and periodic patterns  
- **Normalization:** Improved cross-model consistency and convergence  

### 🤖 Model Training  
- **Classic Models:** *kNN, Random Forest
- **Deep Model:** *TF-C (Contrastive Learning)* — pre-trained on **HAR**, fine-tuned on **Gesture** data  

---

## 📊 Results  

| Model | Features Used | Accuracy | F1-Score |
|:------|:---------------|:---------|:----------|
| **kNN (k=3)** | Normalized + Seasonal | **91.67%** | **91.62%** |
| Random Forest | Raw | 85% | 84% |
| TF-C | Fine-tuned | Lower than expected | – |

---

## 💡 Key Insights  

- 🥇 **Best model:** kNN with normalized and seasonally decomposed features  
- ⚙️ **Feature scaling & decomposition** were crucial for boosting performance  
- 🧠 **Contrastive Learning (TF-C)** underperformed due to limited fine-tuning data and hyperparameter constraints  
