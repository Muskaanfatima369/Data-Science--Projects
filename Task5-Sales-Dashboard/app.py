# ============================================================
# TASK 5: Interactive Business Dashboard — Streamlit
# Dataset: Global Superstore (generated locally)
# Goal: Interactive BI dashboard with filters and KPIs
# Run with: streamlit run app.py
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


# ── PAGE CONFIGURATION ────────────────────────────────────
# Must be the FIRST streamlit command
st.set_page_config(
    page_title="Sales Dashboard — DevelopersHub",
    page_icon="📊",
    layout="wide",              # Use full screen width
    initial_sidebar_state="expanded"
)


# ── GENERATE DATASET ──────────────────────────────────────
# We generate realistic superstore data locally
# No internet or CSV file needed

@st.cache_data                  # Cache so data isn't regenerated on every click
def generate_data():
    np.random.seed(42)
    n = 2000                    # 2000 orders

    # Date range: 2021 to 2024
    start_date = datetime(2021, 1, 1)
    dates = [start_date + timedelta(days=int(x))
             for x in np.random.randint(0, 1460, n)]

    regions     = ['West', 'East', 'Central', 'South']
    categories  = ['Technology', 'Furniture', 'Office Supplies']
    sub_cats    = {
        'Technology'     : ['Phones', 'Computers', 'Accessories', 'Copiers'],
        'Furniture'      : ['Chairs', 'Tables', 'Bookcases', 'Furnishings'],
        'Office Supplies': ['Paper', 'Binders', 'Storage', 'Appliances']
    }
    segments    = ['Consumer', 'Corporate', 'Home Office']
    customers   = [f'Customer_{i:03d}' for i in range(1, 101)]

    # Generate base data
    category_list = np.random.choice(categories, n)
    sub_cat_list  = [np.random.choice(sub_cats[c]) for c in category_list]

    # Sales vary by category
    sales_base = {
        'Technology'     : (500, 3000),
        'Furniture'      : (200, 2000),
        'Office Supplies': (20,  500)
    }
    sales_list = [
        np.random.randint(*sales_base[c])
        for c in category_list
    ]

    # Profit is roughly 10-20% of sales (can be negative)
    profit_list = [
        s * np.random.uniform(-0.05, 0.30)
        for s in sales_list
    ]

    df = pd.DataFrame({
        'Order Date'   : dates,
        'Region'       : np.random.choice(regions, n),
        'Segment'      : np.random.choice(segments, n),
        'Category'     : category_list,
        'Sub-Category' : sub_cat_list,
        'Customer Name': np.random.choice(customers, n),
        'Sales'        : np.round(sales_list, 2),
        'Profit'       : np.round(profit_list, 2),
        'Quantity'     : np.random.randint(1, 10, n)
    })

    # Add month and year columns for filtering
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Year']       = df['Order Date'].dt.year
    df['Month']      = df['Order Date'].dt.month
    df['MonthName']  = df['Order Date'].dt.strftime('%b')

    return df


# ── LOAD DATA ─────────────────────────────────────────────
df = generate_data()


# ── CUSTOM CSS STYLING ────────────────────────────────────
# Make the dashboard look professional
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; }

    /* KPI card style */
    .kpi-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4f8bf9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .kpi-value {
        font-size: 28px;
        font-weight: bold;
        color: #1f2d3d;
    }
    .kpi-label {
        font-size: 13px;
        color: #7f8c8d;
        margin-top: 4px;
    }

    /* Header */
    .dashboard-header {
        background: linear-gradient(90deg, #1f2d3d, #4f8bf9);
        color: white;
        padding: 20px 30px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# ── DASHBOARD HEADER ──────────────────────────────────────
st.markdown("""
    <div class="dashboard-header">
        <h1 style="margin:0; color:white;">📊 Sales Analytics Dashboard</h1>
        <p style="margin:0; opacity:0.8;">
            DevelopersHub Corporation — Data Science Internship Task 5
        </p>
    </div>
""", unsafe_allow_html=True)


# ── SIDEBAR FILTERS ───────────────────────────────────────
st.sidebar.title("🔽 Filters")
st.sidebar.markdown("Use filters to explore the data")

# Region filter
regions_available = ['All'] + sorted(df['Region'].unique().tolist())
selected_region   = st.sidebar.selectbox("🌍 Region", regions_available)

# Category filter
categories_available = ['All'] + sorted(df['Category'].unique().tolist())
selected_category    = st.sidebar.selectbox("📦 Category", categories_available)

# Sub-Category filter (depends on Category)
if selected_category != 'All':
    sub_cats_available = ['All'] + sorted(
        df[df['Category'] == selected_category]['Sub-Category'].unique().tolist()
    )
else:
    sub_cats_available = ['All'] + sorted(df['Sub-Category'].unique().tolist())
selected_subcat = st.sidebar.selectbox("🏷️ Sub-Category", sub_cats_available)

# Segment filter
segments_available = ['All'] + sorted(df['Segment'].unique().tolist())
selected_segment   = st.sidebar.selectbox("👥 Segment", segments_available)

# Year filter
years_available = ['All'] + sorted(df['Year'].unique().tolist())
selected_year   = st.sidebar.selectbox("📅 Year", years_available)

st.sidebar.markdown("---")
st.sidebar.markdown("**📌 About**")
st.sidebar.markdown("""
Built by **Muskan Fatima**
Data Science Intern
DevelopersHub Corporation
""")


# ── APPLY FILTERS ─────────────────────────────────────────
# Filter the dataframe based on sidebar selections
filtered_df = df.copy()

if selected_region   != 'All':
    filtered_df = filtered_df[filtered_df['Region']       == selected_region]
if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['Category']     == selected_category]
if selected_subcat   != 'All':
    filtered_df = filtered_df[filtered_df['Sub-Category'] == selected_subcat]
if selected_segment  != 'All':
    filtered_df = filtered_df[filtered_df['Segment']      == selected_segment]
if selected_year     != 'All':
    filtered_df = filtered_df[filtered_df['Year']         == selected_year]

# Show record count
st.caption(f"📋 Showing **{len(filtered_df):,}** records after filters")


# ── KPI CARDS ─────────────────────────────────────────────
st.markdown("### 📌 Key Performance Indicators")

# Calculate KPIs
total_sales   = filtered_df['Sales'].sum()
total_profit  = filtered_df['Profit'].sum()
total_orders  = len(filtered_df)
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
total_qty     = filtered_df['Quantity'].sum()

# Display in 5 columns
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric(
        label="💰 Total Sales",
        value=f"${total_sales:,.0f}"
    )
with k2:
    st.metric(
        label="📈 Total Profit",
        value=f"${total_profit:,.0f}",
        delta=f"{profit_margin:.1f}% margin"
    )
with k3:
    st.metric(
        label="🛒 Total Orders",
        value=f"{total_orders:,}"
    )
with k4:
    st.metric(
        label="📦 Total Quantity",
        value=f"{total_qty:,}"
    )
with k5:
    avg_order = total_sales / total_orders if total_orders > 0 else 0
    st.metric(
        label="🧾 Avg Order Value",
        value=f"${avg_order:,.0f}"
    )

st.markdown("---")


# ── ROW 1: TWO CHARTS SIDE BY SIDE ───────────────────────
col1, col2 = st.columns(2)

# Chart 1: Sales by Category
with col1:
    st.markdown("#### 📦 Sales by Category")
    cat_sales = (
        filtered_df.groupby('Category')['Sales']
        .sum()
        .reset_index()
        .sort_values('Sales', ascending=False)
    )
    fig1 = px.bar(
        cat_sales,
        x='Category', y='Sales',
        color='Category',
        color_discrete_sequence=px.colors.qualitative.Set2,
        text_auto='.2s'         # Show values on bars
    )
    fig1.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        yaxis_title="Sales ($)",
        xaxis_title=""
    )
    st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Profit by Region
with col2:
    st.markdown("#### 🌍 Profit by Region")
    region_profit = (
        filtered_df.groupby('Region')['Profit']
        .sum()
        .reset_index()
        .sort_values('Profit', ascending=False)
    )
    fig2 = px.bar(
        region_profit,
        x='Region', y='Profit',
        color='Profit',
        color_continuous_scale='RdYlGn',  # Red=loss, Green=profit
        text_auto='.2s'
    )
    fig2.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        yaxis_title="Profit ($)",
        xaxis_title=""
    )
    st.plotly_chart(fig2, use_container_width=True)


# ── ROW 2: MONTHLY SALES TREND ────────────────────────────
st.markdown("#### 📅 Monthly Sales Trend")

monthly = (
    filtered_df.groupby(['Year', 'Month'])['Sales']
    .sum()
    .reset_index()
    .sort_values(['Year', 'Month'])
)
monthly['Period'] = (
    monthly['Year'].astype(str) + '-' +
    monthly['Month'].astype(str).str.zfill(2)
)

fig3 = px.line(
    monthly,
    x='Period', y='Sales',
    markers=True,
    color_discrete_sequence=['#4f8bf9']
)
fig3.update_layout(
    plot_bgcolor='white',
    xaxis_title="Month",
    yaxis_title="Sales ($)",
    xaxis_tickangle=45
)
fig3.update_traces(line_width=2.5)
st.plotly_chart(fig3, use_container_width=True)


# ── ROW 3: TWO MORE CHARTS ────────────────────────────────
col3, col4 = st.columns(2)

# Chart 4: Top 5 Customers by Sales
with col3:
    st.markdown("#### 🏆 Top 5 Customers by Sales")
    top_customers = (
        filtered_df.groupby('Customer Name')['Sales']
        .sum()
        .reset_index()
        .sort_values('Sales', ascending=False)
        .head(5)
    )
    fig4 = px.bar(
        top_customers,
        x='Sales', y='Customer Name',
        orientation='h',            # Horizontal bar chart
        color='Sales',
        color_continuous_scale='Blues',
        text_auto='.2s'
    )
    fig4.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        xaxis_title="Total Sales ($)",
        yaxis_title="",
        yaxis={'categoryorder': 'total ascending'}
    )
    st.plotly_chart(fig4, use_container_width=True)

# Chart 5: Sales by Segment (Pie Chart)
with col4:
    st.markdown("#### 👥 Sales by Customer Segment")
    segment_sales = (
        filtered_df.groupby('Segment')['Sales']
        .sum()
        .reset_index()
    )
    fig5 = px.pie(
        segment_sales,
        values='Sales',
        names='Segment',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4                    # Donut chart
    )
    fig5.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig5, use_container_width=True)


# ── ROW 4: SALES vs PROFIT SCATTER ────────────────────────
st.markdown("#### 💹 Sales vs Profit by Sub-Category")

subcat_data = (
    filtered_df.groupby(['Sub-Category', 'Category'])
    .agg({'Sales': 'sum', 'Profit': 'sum', 'Quantity': 'sum'})
    .reset_index()
)

fig6 = px.scatter(
    subcat_data,
    x='Sales', y='Profit',
    size='Quantity',            # Bubble size = quantity sold
    color='Category',
    hover_name='Sub-Category',  # Show name on hover
    color_discrete_sequence=px.colors.qualitative.Set1,
    size_max=40
)
fig6.add_hline(
    y=0, line_dash='dash',
    line_color='red',
    annotation_text='Break-even line'
)
fig6.update_layout(
    plot_bgcolor='white',
    xaxis_title="Total Sales ($)",
    yaxis_title="Total Profit ($)"
)
st.plotly_chart(fig6, use_container_width=True)


# ── ROW 5: RAW DATA TABLE ─────────────────────────────────
st.markdown("#### 🗃️ Raw Data")

# Toggle to show/hide raw data
if st.checkbox("Show raw data table"):
    st.dataframe(
        filtered_df.sort_values('Order Date', ascending=False),
        use_container_width=True,
        height=300
    )

    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_sales_data.csv',
        mime='text/csv'
    )


# ── FOOTER ────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#7f8c8d; font-size:13px;'>
    📊 Sales Analytics Dashboard |
    Built by <b>Muskan Fatima</b> |
    Data Science Internship — DevelopersHub Corporation 2026
</div>
""", unsafe_allow_html=True)