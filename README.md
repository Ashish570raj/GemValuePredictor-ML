# 💎 Gemstone Price Predictor — ML Web App

A end-to-end Machine Learning project that predicts **diamond prices** based on physical and quality attributes.  
Built with **CatBoost Regressor** and deployed as an interactive **Streamlit** web app.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![CatBoost](https://img.shields.io/badge/Model-CatBoost-yellow)](https://catboost.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Project Overview

The goal is to accurately predict the **price of a diamond** given its characteristics.  
8 regression models were benchmarked end-to-end, with **CatBoost Regressor** achieving the best performance at **R² = 0.9793**.

---

## ▪ Model Performance Comparison

| Model                     | MAE       | RMSE      | R² Score   |
|---------------------------|-----------|-----------|------------|
| **CatBoost Regressor** ✓  | **294.65** | **578.51** | **0.9793** |
| XGB Regressor              | 296.98    | 585.52    | 0.9788     |
| Random Forest Regressor    | 309.06    | 605.76    | 0.9773     |
| K-Neighbors Regressor      | 349.47    | 671.29    | 0.9721     |
| Decision Tree              | 422.17    | 831.62    | 0.9572     |
| Linear Regression          | 671.59    | 1006.60   | 0.9373     |
| Ridge                      | 671.61    | 1006.61   | 0.9373     |
| Lasso                      | 672.86    | 1006.87   | 0.9373     |

> **Final model:** CatBoost Regressor saved as `1_final_model.pkl`

---

## 🎛️ Input Features

| Feature     | Type        | Description                                              |
|-------------|-------------|----------------------------------------------------------|
| `carat`     | Numerical   | Weight of the diamond                                    |
| `cut`       | Categorical | Cut quality — Fair → Good → Very Good → Premium → Ideal  |
| `color`     | Categorical | Color grade — J (worst) → D (best)                       |
| `clarity`   | Categorical | Clarity grade — I1 (worst) → IF (best)                   |
| `depth`     | Numerical   | Total depth percentage                                   |
| `table`     | Numerical   | Width of top facet relative to widest point              |
| `x`         | Numerical   | Length in mm                                             |
| `y`         | Numerical   | Width in mm                                              |
| `z`         | Numerical   | Depth in mm                                              |

---

## 🛠️ Tech Stack

| Category       | Tools                                      |
|----------------|--------------------------------------------|
| Language       | Python 3.11                                |
| ML Framework   | Scikit-learn, CatBoost, XGBoost            |
| Data           | Pandas, NumPy                              |
| Visualization  | Matplotlib, Seaborn, Plotly                |
| Web App        | Streamlit                                  |
| Serialization  | Joblib                                     |

---

## 📁 Project Structure

- `1_EDA.ipynb` — exploratory data analysis, feature insights, and visualizations
- `2__modeltrain.ipynb` — model development, training, hyperparameter tuning, and evaluation
- `main.py` — Streamlit app for interactive diamond price prediction
- `README.md` — project documentation and usage instructions
- `requirements.txt` — Python dependencies
- `train.csv` — training dataset
- `test.csv` — test dataset
- `diamond_cleaned.csv` — cleaned dataset used for modeling
- `sample_submission.csv` — sample submission format
- `1_final_model.pkl` — final trained CatBoost model
- `catboost_info/` — CatBoost training logs and artifacts
- `gemenv/` — local Python virtual environment

---

## 🚀 Getting Started

1. Create and activate a Python environment:
   ```bash
   python -m venv gemenv
   gemenv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
4. Open the provided local URL in your browser and enter diamond details to predict price.

---

## 🧠 What’s Included

- Data preparation and cleaning for diamond pricing data
- Exploratory data analysis to inspect distributions, outliers, and feature relationships
- Feature engineering for categorical encoding and numeric predictors
- Model benchmarking across eight regression algorithms
- Final production-ready model using CatBoost Regressor
- Interactive web app for live price prediction

---

## 📌 Notes

- The final model is saved as `1_final_model.pkl`.
- `main.py` loads the saved model and accepts the same feature set used during training.
- `diamond_cleaned.csv` can be used to reproduce analysis, while `train.csv` and `test.csv` represent the original competition-style datasets.

---

## 📚 Recommended Next Steps

- Review `1_EDA.ipynb` to inspect the EDA flow and confirm data cleaning decisions.
- Review `2__modeltrain.ipynb` to see how model selection and evaluation were performed.
- Update `requirements.txt` if additional packages are needed for your environment.

