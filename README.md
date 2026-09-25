# 🌍 World Development Clustering

## 📌 Project Overview

This project uses machine learning to group countries based on their development indicators.

The project applies **K-Means Clustering** to identify groups of countries with similar development characteristics.

## 🎯 Objective

The main objective is to analyze world development data and classify countries into different clusters based on their development indicators.

## 📊 Dataset

The dataset contains various development-related indicators such as:

- Birth Rate
- Business Tax Rate
- CO2 Emissions
- Days to Start Business
- Other economic and social development indicators

## 🔍 Exploratory Data Analysis

The dataset was explored using:

- Pandas
- Matplotlib
- Seaborn

The analysis included checking:

- Dataset shape
- Data types
- Missing values
- Statistical information
- Feature distributions
- Relationships between variables

## 🤖 Machine Learning

### K-Means Clustering

K-Means clustering was used to group countries based on their development indicators.

Before clustering, the numerical features were standardized using **StandardScaler**.

The trained clustering model and scaler are saved as:

- `kmeans_model.pkl`
- `scaler.pkl`

## 🖥️ Streamlit Application

A Streamlit web application was developed to allow users to enter development indicators and predict the corresponding cluster.

The application is available in:

`app.py`

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook

## 📁 Project Files

| File | Description |
|---|---|
| `Clustering_World_Development.ipynb` | Data analysis and clustering notebook |
| `World_development_measurement (1).xlsx` | Dataset |
| `app.py` | Streamlit application |
| `kmeans_model.pkl` | Trained K-Means model |
| `scaler.pkl` | Feature scaling model |
| `requirements.txt` | Required Python libraries |

## 🚀 How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
### Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

### Project Workflow

1. Load the World Development dataset.
2. Clean and preprocess the data.
3. Select development-related features.
4. Scale the features using StandardScaler.
5. Apply K-Means clustering.
6. Save the trained model and scaler.
7. Use Streamlit to predict the cluster for new input data.

### Output

The application predicts the cluster for the given development indicators.




