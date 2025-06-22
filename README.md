# inventory-demand-forecasting
📦 End-to-end Inventory Demand Forecasting system for supply chain &amp; logistics using LSTM, Prophet, Power BI, Azure, and MS SQL Server – optimized for Canadian job market requirements.
# 📦 Inventory Demand Forecasting – Supply Chain & Logistics

**End-to-end demand forecasting system** for warehouse inventory, built using LSTM, Prophet, Power BI, MS SQL, and Azure. Designed to optimize stock planning in the supply chain and logistics industry, this project integrates calendar, weather, and holiday effects for accurate multi-warehouse forecasts.

---

## 🚀 Project Overview

**Industry**: Supply Chain & Logistics  
**Problem**: Stockouts and overstocking due to poor demand prediction  
**Solution**: Forecast inventory demand using time series models and external factors such as:
- Weather conditions (temperature, precipitation)
- Holidays & weekends
- Day-of-week & month seasonality

---

## 🔧 Tools & Technologies

| Domain | Stack |
|--------|-------|
| **Languages** | Python, SQL (MS SQL Server), R |
| **ML Models** | LSTM (Keras/TensorFlow), Prophet (Facebook) |
| **Visualization** | Power BI, Matplotlib |
| **Cloud** | Azure SQL DB, Azure Blob Storage |
| **UI & Deployment** | Streamlit |
| **Version Control** | Git + GitHub |

---

## 📁 Folder Structure

```bash

inventory-demand-forecasting/
├── data/
│ ├── raw/ # Unprocessed CSVs
│ ├── processed/ # Cleaned datasets
│ └── external/ # Weather and holidays
│
├── database/
│ └── schema.sql # MS SQL schema
│
├── dashboards/
│ └── powerbi/
│ └── inventory_dashboard.pbix
│
├── models/
│ └── lstm_inventory_model.h5
│
├── notebooks/
│ └── demand_forecasting.ipynb
│
├── src/
│ ├── azure_connector.py
│ ├── data_loader.py
│ ├── feature_engineer.py
│ ├── model_lstm.py
│ └── model_prophet.py
│
├── app/
│ └── streamlit_app.py
│
├── dwh_schema.sql
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

## 📊 Power BI Dashboard

The Power BI dashboard includes:
- 📈 Forecast vs Actual Demand
- 🧊 Weather overlay (precipitation & temperature)
- 🚨 Stock Level Warnings
- 📍 Warehouse-wise Performance

> File: `dashboards/powerbi/inventory_dashboard.pbix`

---

## 📚 How to Run

### 🔹 1. Clone the Repo
```bash
git clone https://github.com/yourusername/inventory-demand-forecasting.git
cd inventory-demand-forecasting
```

```bash
pip install -r requirements.txt
```
🔹 3. Load Data into Azure SQL
Use database/schema.sql to set up your database tables

Upload cleaned data from data/processed/

🔹 4. Run the Notebook

```bash
jupyter notebook notebooks/demand_forecasting.ipynb
```
🔹 5. Launch Streamlit App
```bash
streamlit run app/streamlit_app.py
```
☁️ Azure Integration
Azure SQL Database for storing historical sales and external features

Azure Blob Storage (optional) for uploading raw files

Streamlit app can be deployed on Azure App Services using az webapp up

🧠 Models Used
✅ Prophet
Captures seasonality and holiday effects

Quick, interpretable, and business-friendly

✅ LSTM (Long Short-Term Memory)
Neural network-based deep forecasting model

Good for capturing complex sequential patterns