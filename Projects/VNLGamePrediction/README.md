# 🏐 Volleyball Nations League (VNL) Prediction using Feature Imitation

A deep learning project predicting **VNL match outcomes** using individual player statistics and a **Feature Imitation Network (FIN)**-inspired architecture. Developed as part of academic coursework at the **University of Wrocław**.

---

## 🎯 Project Overview

- **Goal:** Predict volleyball match results (win/loss) using team and player stats.  
- **Approach:** Compare complex FIN-inspired architectures vs. simpler baseline models.  
- **Architecture:** MambaNet incorporates **LSTM**, **Conv1D**, and FIN-inspired layers to process player-level features.  

### 🧩 Key Objectives
- Build an accurate predictive model for VNL matches.  
- Evaluate the impact of FIN-inspired feature aggregation.  
- Compare FIN-based and baseline models using multiple performance metrics.  

---

## 👥 Team

- Mateusz Budzyński  
- Maciej Ciepiela  
- Mikołaj Komarnicki  

---

## 📓 Notebook Highlights – `VNL_pred.ipynb`

### 🔍 Data & Preprocessing
- **Sources:** Kaggle datasets (VNL 2021–2023) + manually scraped Wikipedia data  
- **Input:** Player-level stats aggregated to team-level  
- **Cleaning & Structuring:** Preprocessing for ML-ready inputs  

### ⚙️ Model Architectures
- **MambaNet:** FIN-inspired network (LSTM + Conv1D + FIN for player stats)  
- **wo_fins:** Same network without FIN component  
- **Simple:** Baseline network without complex feature processing  

### 🤖 Training & Evaluation
- **GPU-accelerated** training (Google Colab recommended)  
- **Metrics:** Accuracy, F1-Score, Precision, Recall  

---
