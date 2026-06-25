import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Air Quality Awareness Assistant",
    page_icon="🌍",
    layout="wide"
)

# Load Model
model = joblib.load("air_quality_model.pkl")

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f4f8fb;
}

h1 {
    color: #0d47a1;
    text-align: center;
}

[data-testid="stMetricValue"] {
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌍 Project Information")

st.sidebar.write("""
### Air Quality Awareness Assistant

**AI Model:** Random Forest Classifier

**Accuracy:** 93.98%

**Developed For:**
1M1B AI for Sustainability Internship

### Supported SDGs
✅ SDG 3 - Good Health & Well-being

✅ SDG 11 - Sustainable Cities

✅ SDG 13 - Climate Action
""")

# Banner
st.markdown("""
<div style='background:linear-gradient(90deg,#0d47a1,#42a5f5);
padding:30px;border-radius:15px;color:white;text-align:center'>
<h1>🌍 Air Quality Awareness Assistant</h1>
<h3>AI-Powered Solution for Cleaner Air & Sustainable Communities</h3>
<p>Predict Air Quality • Get Health Recommendations • Promote Sustainability</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Welcome Card
st.markdown("""
<div style='background-color:#e8f5e9;
padding:20px;
border-radius:15px;
text-align:center'>
<h2>Welcome to the Future of Environmental Awareness 🌱</h2>
<p>
This AI-powered assistant predicts air quality levels using environmental sensor data
and helps users take informed actions for healthier living.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", "93.98%")

with col2:
    st.metric("Dataset Records", "9,357")

with col3:
    st.metric("SDGs Supported", "3")

st.write("")

# Why Air Quality Matters
st.subheader("🎯 Why Air Quality Matters")

st.info("""
Air pollution affects millions of people every year.

Poor air quality can lead to respiratory diseases, heart problems,
and environmental damage.

This AI-powered assistant helps users understand air quality levels
and take preventive actions.
""")

# Features
st.subheader("🚀 Key Features")

st.write("✅ AI-Powered Air Quality Prediction")
st.write("✅ Health Recommendations")
st.write("✅ Pollution Visualization Dashboard")
st.write("✅ Sustainability Awareness Tips")
st.write("✅ Interactive User-Friendly Interface")

# SDG Section
st.subheader("🌱 Sustainable Development Goals")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("SDG 3\n\nGood Health & Well-being")

with c2:
    st.success("SDG 11\n\nSustainable Cities")

with c3:
    st.success("SDG 13\n\nClimate Action")

st.write("---")

# Input Section
st.subheader("📊 Enter Air Quality Parameters")

pt08 = st.number_input("PT08.S1(CO)", value=1000.0)
nmhc = st.number_input("NMHC(GT)", value=100.0)
c6h6 = st.number_input("C6H6(GT)", value=10.0)
pt08_s2 = st.number_input("PT08.S2(NMHC)", value=900.0)
nox = st.number_input("NOx(GT)", value=100.0)
pt08_s3 = st.number_input("PT08.S3(NOx)", value=1000.0)
no2 = st.number_input("NO2(GT)", value=100.0)
pt08_s4 = st.number_input("PT08.S4(NO2)", value=1500.0)
pt08_s5 = st.number_input("PT08.S5(O3)", value=1000.0)
temp = st.number_input("Temperature (T)", value=20.0)
rh = st.number_input("Relative Humidity (RH)", value=50.0)
ah = st.number_input("Absolute Humidity (AH)", value=1.0)

# Prediction
if st.button("🔍 Predict Air Quality"):

    data = pd.DataFrame([[
        pt08,
        nmhc,
        c6h6,
        pt08_s2,
        nox,
        pt08_s3,
        no2,
        pt08_s4,
        pt08_s5,
        temp,
        rh,
        ah
    ]], columns=[
        "PT08.S1(CO)",
        "NMHC(GT)",
        "C6H6(GT)",
        "PT08.S2(NMHC)",
        "NOx(GT)",
        "PT08.S3(NOx)",
        "NO2(GT)",
        "PT08.S4(NO2)",
        "PT08.S5(O3)",
        "T",
        "RH",
        "AH"
    ])

    prediction = model.predict(data)[0]

    st.write("---")
    st.subheader("📢 Prediction Result")

    if prediction == "Good":
        st.success("🟢 GOOD AIR QUALITY")
        st.balloons()

    elif prediction == "Moderate":
        st.warning("🟡 MODERATE AIR QUALITY")

    else:
        st.error("🔴 POOR AIR QUALITY")

    # AI Insights
    st.subheader("🤖 AI Insights")

    if prediction == "Good":
        st.info("""
        Pollution levels are within acceptable limits.
        Outdoor activities are generally safe.
        """)

    elif prediction == "Moderate":
        st.info("""
        Some pollutants are elevated.
        Sensitive groups should take precautions.
        """)

    else:
        st.info("""
        High pollution detected.
        Health risks may increase with prolonged exposure.
        """)

    # Health Recommendations
    st.subheader("🏥 Health Recommendations")

    if prediction == "Good":
        st.write("✅ Safe for outdoor activities")
        st.write("✅ Walking and exercise recommended")
        st.write("✅ Fresh air conditions")

    elif prediction == "Moderate":
        st.write("⚠ Sensitive people should be careful")
        st.write("⚠ Reduce prolonged outdoor exposure")
        st.write("⚠ Consider wearing a mask")

    else:
        st.write("🚨 Avoid outdoor activities")
        st.write("🚨 Wear N95 masks")
        st.write("🚨 Keep windows closed")
        st.write("🚨 Monitor respiratory symptoms")

    # Charts
    st.subheader("📊 Pollution Parameters Visualization")

    chart_data = pd.DataFrame({
        "Parameter": ["PT08", "NMHC", "NOx", "NO2", "Temp", "RH"],
        "Value": [pt08, nmhc, nox, no2, temp, rh]
    })

    col1, col2 = st.columns(2)

    with col1:
        st.bar_chart(chart_data.set_index("Parameter"))

    with col2:
        st.line_chart(chart_data.set_index("Parameter"))

    # Sustainability Tips
    st.subheader("🌱 Sustainability Tips")

    tips = [
        "Use public transportation.",
        "Plant more trees.",
        "Reduce vehicle emissions.",
        "Save electricity.",
        "Support renewable energy.",
        "Avoid burning waste.",
        "Promote environmental awareness."
    ]

    for tip in tips:
        st.write("✅", tip)

    st.success(
        "Thank you for contributing to a cleaner and healthier environment! 🌍"
    )

st.markdown("---")
st.markdown(
    "### 🌱 Powered by AI for Sustainability | 1M1B Internship Project"
)