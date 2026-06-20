# 📊 Task 1 — Term Deposit Subscription Prediction

## 🎯 Objective
Predict whether a bank customer will subscribe to a term deposit as a result
of a marketing campaign.

---

## 📁 Dataset
- **Source:** Bank Marketing Dataset (UCI Machine Learning Repository)
- **Rows:** 45,211 customer records
- **Target:** `y` — Did customer subscribe? (yes/no)

### Key Features
| Feature | Description |
|---------|-------------|
| `age` | Customer age |
| `job` | Job type |
| `marital` | Marital status |
| `education` | Education level |
| `balance` | Account balance |
| `duration` | Last call duration (seconds) |
| `campaign` | Number of contacts this campaign |

---

## 🔧 Approach

### 1. Data Exploration & Cleaning
- Checked for missing values and data types
- Explored class imbalance (88% No vs 12% Yes)
- Visualized age, job, and marital status distributions

### 2. Feature Encoding
- Label Encoding for all categorical columns
- Target mapped: yes → 1, no → 0

### 3. Model Training
- **Logistic Regression** with `class_weight='balanced'`
- **Random Forest** with `class_weight='balanced'`
- StandardScaler applied for Logistic Regression

### 4. Evaluation
- Confusion Matrix
- Classification Report (Precision, Recall, F1)
- ROC Curve + AUC Score

### 5. Explainable AI (SHAP)
- SHAP TreeExplainer applied to Random Forest
- Summary plot showing global feature importance
- Waterfall plots explaining 5 individual predictions

---

## 📈 Results

| Model | Accuracy | F1 Score | ROC AUC |
|-------|----------|----------|---------|
| Logistic Regression | ~78% | ~0.45 | ~0.83 |
| Random Forest | ~85% | ~0.52 | ~0.88 |

---

## 💡 Key Insights
- Students and retired customers are most likely to subscribe
- Longer call duration strongly correlates with subscription
- Customers with no existing loans subscribe more
- SHAP reveals `duration` and `balance` as top features

---

## 🛠️ Libraries Used
```
pandas, numpy, matplotlib, seaborn
scikit-learn, shap
```

---

## ▶️ How to Run
```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn shap

# Open notebook
jupyter notebook task1_term_deposit.ipynb
```

---

## 📂 Files
```
Task1-Term-Deposit-Prediction/
├── task1_term_deposit.ipynb    ← Main notebook
└── README.md                   ← This file
```

---

*Part of Data Science Internship at DevelopersHub Corporation — June 2026*
