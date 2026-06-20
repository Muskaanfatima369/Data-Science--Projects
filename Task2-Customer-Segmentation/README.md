# 🛍️ Task 2 — Customer Segmentation Using Unsupervised Learning

## 🎯 Objective
Cluster mall customers based on spending habits and propose tailored
marketing strategies for each identified segment.

---

## 📁 Dataset
- **Source:** Mall Customers Dataset
- **Rows:** 200 customer records
- **Type:** No target column — Unsupervised Learning

### Features
| Feature | Description |
|---------|-------------|
| `CustomerID` | Unique customer ID (dropped) |
| `Gender` | Male / Female |
| `Age` | Customer age |
| `Income` | Annual income (k$) |
| `SpendingScore` | Mall-assigned score (1–100) |

---

## 🔧 Approach

### 1. Exploratory Data Analysis
- Gender distribution
- Age and income histograms
- Income vs Spending Score scatter plot
- Spotted 5 natural visual clusters before modeling

### 2. Finding Optimal K — Elbow Method
- Tested K = 1 to 10
- Plotted inertia curve
- Identified elbow at **K = 5**

### 3. K-Means Clustering
- Applied KMeans with K=5
- Assigned cluster labels to each customer
- Analyzed average Income & SpendingScore per cluster

### 4. PCA Visualization
- Reduced 3 features (Age, Income, SpendingScore) to 2D
- Plotted clusters in 2D space using PCA components
- Confirmed clear cluster separation

### 5. Marketing Strategy
- Named each cluster based on profile
- Proposed targeted strategies per segment

---

## 📊 Clusters Found

| Cluster | Profile | Strategy |
|---------|---------|----------|
| VIP | High Income, High Spending | Loyalty rewards, exclusive access |
| Savers | High Income, Low Spending | Discount offers, urgency deals |
| Impulsive | Low Income, High Spending | EMI options, flash sales |
| Budget | Low Income, Low Spending | Coupons, festival promotions |
| Average | Medium Income, Medium Spending | Personalized recommendations |

---

## 💡 Key Insights
- 5 distinct customer groups identified
- Income and Spending Score are most discriminating features
- PCA explains ~85% of total variance in 2 components
- VIP customers need retention; Savers need motivation

---

## 🛠️ Libraries Used
```
pandas, numpy, matplotlib, seaborn
scikit-learn (KMeans, PCA, StandardScaler)
```

---

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn

jupyter notebook task2_segmentation.ipynb
```

---

## 📂 Files
```
Task2-Customer-Segmentation/
├── task2_segmentation.ipynb    ← Main notebook
└── README.md                   ← This file
```

---

*Part of Data Science Internship at DevelopersHub Corporation — June 2026*
