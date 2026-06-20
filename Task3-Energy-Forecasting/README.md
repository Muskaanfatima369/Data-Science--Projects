# ⚡ Task 3 — Energy Consumption Time Series Forecasting

## 🎯 Objective
Forecast short-term household energy usage using historical time-based
patterns by comparing three different forecasting models.

---

## 📁 Dataset
- **Source:** Household Power Consumption Dataset (simulated)
- **Frequency:** Hourly → resampled to Daily
- **Period:** 2 years (2022–2023)
- **Target:** Daily average energy consumption (kWh)

### Features Engineered
| Feature | Description |
|---------|-------------|
| `day_of_week` | 0=Monday to 6=Sunday |
| `month` | 1–12 |
| `day_of_year` | 1–365 |
| `is_weekend` | 1 if Saturday/Sunday |
| `lag_1` | Yesterday's consumption |
| `lag_7` | Same day last week |
| `lag_30` | Same day last month |
| `rolling_7` | 7-day rolling average |
| `rolling_30` | 30-day rolling average |

---

## 🔧 Approach

### 1. Data Generation & EDA
- Generated 2 years of realistic hourly energy data
- Built in morning/evening peaks, weekday/weekend patterns
- Added seasonal variation (summer = higher usage)
- Visualized hourly and monthly consumption patterns

### 2. Resampling
- Converted hourly → daily average
- Reduced 17,520 rows to 730 rows

### 3. Feature Engineering
- Extracted time-based features for XGBoost
- Created lag and rolling average features

### 4. Train/Test Split
- Last 60 days used as test set
- Remaining ~670 days for training

### 5. Model 1 — ARIMA (5,1,2)
- Classical statistical time series model
- Captures autoregression and moving average patterns

### 6. Model 2 — Prophet
- Facebook's forecasting library
- Handles yearly and weekly seasonality automatically
- Plots trend + seasonality components separately

### 7. Model 3 — XGBoost
- ML-based regression using engineered features
- Lag features and rolling averages as inputs
- Feature importance analysis included

---

## 📈 Results

| Model | MAE (kWh) | RMSE (kWh) |
|-------|-----------|------------|
| ARIMA | ~0.18 | ~0.22 |
| Prophet | ~0.15 | ~0.19 |
| XGBoost | ~0.12 | ~0.16 |

*XGBoost performs best with lag and rolling features*

---

## 💡 Key Insights
- Energy peaks at 7–9 AM and 6–10 PM daily
- Summer months consume 80% more than spring/autumn
- Weekends show 30% higher consumption than weekdays
- XGBoost outperforms statistical models with feature engineering
- Prophet best captures seasonal decomposition visually

---

## 🛠️ Libraries Used
```
pandas, numpy, matplotlib, seaborn
statsmodels (ARIMA)
prophet
xgboost
scikit-learn
```

---

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn statsmodels prophet xgboost scikit-learn

jupyter notebook task3_forecasting.ipynb
```

---

## 📂 Files
```
Task3-Energy-Forecasting/
├── task3_forecasting.ipynb     ← Main notebook
└── README.md                   ← This file
```

---

*Part of Data Science Internship at DevelopersHub Corporation — June 2026*
