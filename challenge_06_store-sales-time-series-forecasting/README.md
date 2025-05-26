# 🏪 Store Sales: Time Series Forecasting

This repository contains my work on the [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting) competition hosted on Kaggle.

## 📌 Objective

Forecast daily unit sales for a major Ecuadorian grocery retailer using historical sales data enriched with promotions, holidays, oil prices, and transaction volumes. The challenge is framed as a time series regression problem.

## 📂 Project Structure

.
├── data/ # Local copies of Kaggle data (not tracked by Git)
├── notebooks/ # Jupyter notebooks for EDA and modeling
├── scripts/ # Reusable Python scripts for preprocessing, training, etc.
├── models/ # Saved model weights or serialized pipelines
├── outputs/ # Submission files and logs
└── README.md # Project overview


## 🧠 Key Features to Explore

- Temporal trends and seasonality
- Store and item hierarchies
- Promotions and holidays
- External variables like oil price and transactions

## 🔧 Tools & Technologies

- Python (pandas, numpy, matplotlib, seaborn)
- scikit-learn
- XGBoost / LightGBM
- Prophet / ARIMA (if applicable)
- Kaggle API

## 📈 Evaluation Metric

The competition uses **RMSLE (Root Mean Squared Logarithmic Error)** as the evaluation metric.

## 🚀 Getting Started

1. Download the competition data from the [Kaggle competition page](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)
2. Place all `.csv` files in the `data/` directory
3. Open `notebooks/eda.ipynb` to start exploring the data

## ✅ Goals

- Perform exploratory data analysis
- Build a solid baseline model
- Tune models using validation strategies
- Incorporate time-series features
- Make final predictions for submission
