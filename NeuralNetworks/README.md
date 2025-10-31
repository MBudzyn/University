# 🧠 Neural Networks

This repository contains lab notebooks and project implementations from the **Neural Networks** course at the **University of Wrocław**.  
It explores both **fundamental neural architectures** and **advanced deep learning techniques**, focusing on practical model design, tuning, and evaluation.

---

## 🧭 Overview

The course emphasizes building, training, and analyzing **deep neural networks** from scratch and with **PyTorch**.  
The repository is organized into:

- **`data/`** — Datasets (e.g., MNIST, Oxford Pets) used for training and evaluation  
- **`Tasks/`** — Jupyter notebooks with implementations and experiments for each assignment  

---

## 🧩 Topics Covered

- 🧮 **Core Neural Network Fundamentals** — Forward/backward propagation, gradient computation, NumPy implementation  
- 🧠 **Convolutional Neural Networks (CNNs)** — AlexNet baseline, BatchNorm, Dropout, Hyperparameter tuning, Data augmentation  
- ⚙️ **Optimization Techniques** — Learning rate tuning, optimizers (SGD, Adam), normalization strategies  
- 🔍 **Object Detection (YOLOv5)** — Output tensor interpretation, NMS, IoU thresholding, precision/recall, mAP@0.5  
- 🧬 **Semantic Segmentation (U-Net)** — Binary segmentation, BCE loss, IoU & Dice coefficient, ablation on residuals  
- 🔤 **Word Embeddings (Word2Vec)** — Implementation with negative sampling, gradient clipping, visualization (PCA, t-SNE)  

---

## 🗂️ Folder Structure

```bash
Neural_Networks/
├─ data/                         # Datasets used for training and evaluation
│   └─ MNIST/
│
├─ Tasks/                        # Main assignment notebooks
│   ├─ Assignment1.ipynb         # NumPy NN implementation (forward/backward pass)
│   ├─ Assignment2.ipynb         # CNNs, regularization, and tuning
│   ├─ Assignment3.ipynb         # YOLOv5 object detection and NMS
│   ├─ Assignment4.ipynb         # U-Net for image segmentation
│   ├─ Assignment5.ipynb         # Word2Vec with negative sampling
│   └─ Assignment5_2.ipynb       # Embedding analysis and evaluation
