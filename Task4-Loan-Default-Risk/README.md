# 🏦 Task 4 — Loan Default Risk with Business Cost Optimization

## 🎯 Objective
Predict the likelihood of a loan default and optimize the decision threshold
based on a cost-benefit analysis to minimize total business losses.

---

## 📁 Dataset
- **Source:** Home Credit Default Risk (simulated)
- **Rows:** 5,000 loan applications
- **Target:** `Default` — 1 = Defaulted, 0 = Repaid

### Features
| Feature | Description |
|---------|-------------|
| `Age` | Applicant age |
| `Income` | Annual income ($) |
| `LoanAmount` | Requested loan amount |
| `LoanTerm` | Loan duration (months) |
| `CreditScore` | Credit score (300–850) |
| `Employment` | Employment type |
| `Education` | Education level |
| `MaritalStatus` | Marital status |
| `PastDefaults` | Number of past defaults |
| `DebtRatio` | Debt-to-income ratio |

---

## 🔧 Approach

### 1. Data Exploration & EDA
- Analyzed default rate per employment type
- Credit score distribution by default status
- Income vs default correlation
- Debt ratio impact on defaults
- Full correlation heatmap

### 2. Preprocessing
- Label Encoding for categorical columns
- Stratified train/test split (80/20)
- StandardScaler for Logistic Regression

### 3. Model 1 — Logistic Regression
- Baseline classification model
- `class_weight='balanced'` for imbalanced data
- Evaluated with F1, ROC-AUC

### 4. Model 2 — CatBoost
- Gradient boosting by Yandex
- `auto_class_weights='Balanced'`
- Early stopping to prevent overfitting
- Feature importance extracted

### 5. ROC Curve Comparison
- Both models plotted on same ROC graph
- AUC scores compared

### 6. Business Cost Optimization ⭐
- Defined cost matrix:
  - False Negative (miss a defaulter) = **$10,000 loss**
  - False Positive (reject good loan) = **$500 loss**
- Tested thresholds from 0.1 to 0.9
- Calculated total business cost at each threshold
- Found optimal threshold that minimizes total cost
- Compared cost at optimal vs default (0.5) threshold

---

## 📈 Results

| Model | Accuracy | F1 Score | ROC AUC |
|-------|----------|----------|---------|
| Logistic Regression | ~74% | ~0.51 | ~0.81 |
| CatBoost | ~82% | ~0.63 | ~0.89 |

### Cost Optimization
| Threshold | Total Business Cost |
|-----------|-------------------|
| 0.50 (default) | Higher |
| Optimal (~0.30) | Minimized ✅ |

---

## 💡 Key Insights
- CreditScore and DebtRatio are the strongest default predictors
- Unemployed customers default at 3x the rate of employed ones
- Default threshold of 0.5 is NOT optimal for business
- Lower threshold catches more defaulters, saving significant losses
- CatBoost outperforms Logistic Regression significantly

---

## 🛠️ Libraries Used
```
pandas, numpy, matplotlib, seaborn
scikit-learn (LogisticRegression, metrics)
catboost
```

---

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn catboost

jupyter notebook task4_loan_default.ipynb
```

---

## 📂 Files
```
Task4-Loan-Default-Risk/
├── task4_loan_default.ipynb    ← Main notebook
└── README.md                   ← This file
```

---

*Part of Data Science Internship at DevelopersHub Corporation — June 2026*
