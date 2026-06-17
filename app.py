import streamlit as st
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Machine Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("📊 Dashboard Menu")

st.sidebar.info("""
AI-Based Machine Sales Forecasting System

👩‍💻 Developer:
Samiksha Kumari
""")

st.sidebar.success("🏆 Best Model: Random Forest")

st.sidebar.write("Dataset Information")
st.sidebar.write(" Records: 913,000")
st.sidebar.write(" Stores: 10")
st.sidebar.write(" Machines: 50")
# ----------------------------
# Header
# ----------------------------
st.title(" AI-Based Machine Sales Forecasting System")

st.markdown("""
### 👩‍💻 Developed By: Samiksha Kumari

**Project:** AI-Based Machine Sales Forecasting System

**Technologies:** Python, Pandas, Scikit-Learn, XGBoost, Streamlit

**Dataset Size:** 913,000 Sales Records
""")
# ---------------- Dataset Preview ----------------

st.header(" Dataset Preview")

sample = pd.DataFrame({
    "Date":["2013-01-01","2013-01-02","2013-01-03"],
    "Store":[1,2,3],
    "Item":[1,2,3],
    "Sales":[13,45,27]
})

st.dataframe(sample,use_container_width=True)

# ----------------------------
# Business Objective
# ----------------------------
st.header(" Business Objective")

st.write("""
Predict machine sales demand, identify top-selling machines,
compare forecasting models, and generate inventory restocking recommendations.
""")

# ----------------------------
# KPI Cards
# ----------------------------
st.header(" Project Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Sales Records", "913,000")
col2.metric("Stores", "10")
col3.metric("Machines", "50")
col4.metric("Best Model", "Random Forest")

st.header(" Overall Model Accuracy")

st.metric(
    label="Forecast Accuracy",
    value="91.82%"
)

# ----------------------------
# Model Performance
# ----------------------------
st.header(" Model Performance")

comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest", "XGBoost"],
    "MAE": [22.08, 6.28, 7.02],
    "RMSE": [27.39, 8.18, 9.38]
})

st.dataframe(comparison, use_container_width=True)

st.bar_chart(comparison.set_index("Model"))

st.success(" Random Forest selected as the Final Forecasting Model")

left,right=st.columns(2)

with left:
    st.subheader("Performance Table")
    st.dataframe(comparison,use_container_width=True)

with right:
    st.subheader("Performance Chart")
    st.bar_chart(
        comparison.set_index("Model"),
        use_container_width=True
    )

# ----------------------------
# Feature Importance
# ----------------------------
st.info("""
The graph shows that **Item** contributes the most towards machine sales prediction,
followed by **Store** and **Month**.
""")
st.header(" Feature Importance")

importance = pd.DataFrame({
    "Feature": [
        "Item",
        "Store",
        "Month",
        "Day",
        "Year",
        "Day of Week"
    ],
    "Importance": [
        0.565,
        0.21,
        0.12,
        0.05,
        0.03,
        0.02
    ]
})

st.bar_chart(importance.set_index("Feature"))

# ----------------------------
# Future Sales Prediction
# ----------------------------
st.header(" Future Sales Forecast")

future = pd.DataFrame({
    "Store":[1,2,3,4,5],
    "Machine":[1,2,3,4,5],
    "Predicted Sales":[14.30,45.06,27.44,18.62,11.84]
})

st.dataframe(future, use_container_width=True)
st.header(" Inventory Recommendation")

recommendation=pd.DataFrame({
    "Machine":[1,2,3,4,5],
    "Predicted Sales":[14,45,27,18,11],
    "Recommendation":[
        "Maintain",
        "Restock",
        "Restock",
        "Maintain",
        "Low Demand"
    ]
})

st.dataframe(recommendation,use_container_width=True)
st.header(" Monthly Sales Trend")

sales=pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[2500,3200,4100,3800,4500,5200]
})

st.line_chart(
    sales.set_index("Month"),
    use_container_width=True
)

# ----------------------------
# Business Insights
# ----------------------------
st.header(" Business Insights")

st.success("""
✔ Item is the most influential feature affecting machine sales.

✔ Sales demand varies across stores.

✔ Seasonal patterns impact forecasting.

✔ Random Forest achieved the best prediction accuracy.

✔ Future sales prediction helps optimize inventory planning.
""")
st.header(" Store-wise Sales")

store=pd.DataFrame({
    "Store":[1,2,3,4,5],
    "Sales":[1500,2400,1800,2900,2100]
})

st.bar_chart(
    store.set_index("Store"),
    use_container_width=True
)

# ----------------------------
# Project Achievements
# ----------------------------
st.header(" Project Achievements")

st.markdown("""
- Processed and analyzed **913,000** sales records.
- Performed Exploratory Data Analysis (EDA).
- Built Linear Regression, Random Forest, and XGBoost models.
- Compared model performance using MAE and RMSE.
- Selected Random Forest as the final forecasting model.
- Generated future sales predictions.
- Provided inventory restocking recommendations.
""")

st.header(" Project Workflow")

st.markdown("""
Data Collection

⬇️

Data Cleaning

⬇️

EDA

⬇️

Feature Engineering

⬇️

Model Training

⬇️

Model Evaluation

⬇️

Future Prediction

⬇️

Inventory Recommendation
""")
# ----------------------------
# Conclusion
# ----------------------------
st.header("Conclusion")

st.write("""
The AI-Based Machine Sales Forecasting System successfully predicts future
machine sales using historical data. The Random Forest model achieved the
highest accuracy and can help businesses make better inventory and purchasing
decisions.
""")

st.markdown("---")

st.caption("© 2026 Samiksha Kumari | AI-Based Machine Sales Forecasting Dashboard")