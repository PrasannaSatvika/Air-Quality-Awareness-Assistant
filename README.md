# 🌍 Air Quality Awareness Assistant

## 📌 Project Overview

Air Quality Awareness Assistant is an AI-powered web application developed to predict air quality levels using environmental sensor data. The system helps users understand air pollution conditions, receive health recommendations, and promote sustainable environmental practices.

This project was developed as part of the **1M1B AI for Sustainability Virtual Internship Program**.

---

## 🎯 Problem Statement

Air pollution is one of the major environmental challenges affecting human health and the ecosystem. Many people are unaware of the quality of air around them and the health risks associated with pollution.

This project uses Machine Learning to analyze air quality parameters and provide awareness through easy-to-understand predictions and recommendations.

---

## 🚀 Features

* 🤖 AI-Based Air Quality Prediction
* 📊 Interactive Streamlit Dashboard
* 🏥 Health Recommendations
* 🌱 Sustainability Awareness Tips
* 📈 Pollution Visualization Charts
* 🎯 SDG-Focused Solution

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Joblib

---

## 🧠 Machine Learning Model

**Algorithm:** Random Forest Classifier

**Model Accuracy:** 93.98%

### Input Parameters

* PT08.S1(CO)
* NMHC(GT)
* C6H6(GT)
* PT08.S2(NMHC)
* NOx(GT)
* PT08.S3(NOx)
* NO2(GT)
* PT08.S4(NO2)
* PT08.S5(O3)
* Temperature (T)
* Relative Humidity (RH)
* Absolute Humidity (AH)

### Output

* Good Air Quality
* Moderate Air Quality
* Poor Air Quality

---

## 🌱 Sustainable Development Goals (SDGs)

This project supports:

* SDG 3: Good Health and Well-being
* SDG 11: Sustainable Cities and Communities
* SDG 13: Climate Action

---

## 📂 Project Structure

```text
Air Quality Awareness Assistant
│
├── app.py
├── train_model.py
├── clean_data.py
├── save_model.py
├── air_quality_model.pkl
├── AirQuality.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Dashboard Features

* User-friendly interface
* Air quality prediction
* Pollution parameter visualization
* Health recommendations
* Sustainability tips

---

## 📈 Future Scope

* Real-time AQI integration
* IoT sensor connectivity
* Mobile application support
* Smart city implementation
* Location-based pollution alerts

---

## 👩‍💻 Developed By

**Prasanna Satvika**

B.Tech Computer Science Engineering

Project: Air Quality Awareness Assistant

1M1B AI for Sustainability Internship

---

## 🌍 Conclusion

The Air Quality Awareness Assistant demonstrates how Artificial Intelligence can be used to address environmental challenges. By predicting air quality and providing actionable recommendations, the project contributes toward healthier communities and sustainable living.
