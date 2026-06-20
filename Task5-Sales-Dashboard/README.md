# 📊 Task 5 — Interactive Business Dashboard in Streamlit

## 🎯 Objective
Develop an interactive dashboard for analyzing sales, profit, and
segment-wise performance using the Global Superstore dataset.

---

## 📁 Dataset
- **Source:** Global Superstore Dataset
- **Content:** Sales transactions with region, category, and customer data
- **Target:** No ML — Business Intelligence & Visualization

### Key Columns
| Column | Description |
|--------|-------------|
| `Order Date` | Date of order |
| `Region` | Geographic region |
| `Category` | Product category |
| `Sub-Category` | Product sub-category |
| `Sales` | Sale amount ($) |
| `Profit` | Profit amount ($) |
| `Customer Name` | Customer name |
| `Segment` | Customer segment |

---

## 🔧 Approach

### 1. Data Cleaning
- Parsed date columns correctly
- Handled missing values
- Removed duplicate orders

### 2. Streamlit Dashboard Features
- **Sidebar Filters:**
  - Region selector
  - Category selector
  - Sub-Category selector
  - Date range picker

- **KPI Cards:**
  - 💰 Total Sales
  - 📈 Total Profit
  - 🛒 Total Orders
  - 📊 Profit Margin %

- **Charts:**
  - Sales by Category (Bar Chart)
  - Monthly Sales Trend (Line Chart)
  - Top 5 Customers by Sales (Horizontal Bar)
  - Profit by Region (Bar Chart)
  - Sales vs Profit Scatter Plot

---

## 🖥️ Dashboard Preview

```
┌─────────────────────────────────────────────────┐
│  FILTERS (Sidebar)    │    KPI CARDS            │
│  Region:  [All ▼]     │  Sales: $2.3M           │
│  Category:[All ▼]     │  Profit: $286K          │
│  Sub-Cat: [All ▼]     │  Orders: 9,994          │
│                       │  Margin: 12.5%          │
├───────────────────────┴─────────────────────────┤
│  [Sales by Category]    [Monthly Sales Trend]   │
├─────────────────────────────────────────────────┤
│  [Top 5 Customers]      [Profit by Region]      │
└─────────────────────────────────────────────────┘
```

---

## 💡 Key Insights
- Technology category generates highest sales
- West region leads in both sales and profit
- Office Supplies have highest order volume
- Top customer contributes significantly to total revenue
- Q4 consistently shows peak sales performance

---

## 🛠️ Libraries Used
```
pandas, numpy
streamlit
plotly
```

---

## ▶️ How to Run

```bash
# Install dependencies
pip install pandas numpy streamlit plotly

# Run the dashboard
streamlit run app.py
```

Then open your browser at: `http://localhost:8501`

---

## 📂 Files
```
Task5-Sales-Dashboard/
├── app.py          ← Streamlit dashboard code
├── README.md       ← This file
└── superstore.csv  ← Dataset (if downloaded)
```

---

*Part of Data Science Internship at DevelopersHub Corporation — June 2026*
