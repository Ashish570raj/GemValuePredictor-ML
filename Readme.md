# Gemstone Price Prediction using Machine Learning

A Machine Learning web app built using **CatBoost Regressor** to predict gemstone (diamond) prices based on key attributes such as **carat, cut, color, clarity, depth, and table**.  
This project is deployed using **Streamlit Cloud** and allows users to interactively input gemstone features and instantly get the predicted price.

---

##  Project Overview

The goal of this project is to accurately predict the **price of diamonds** based on their physical characteristics and quality attributes.  
Multiple regression models were tested — including Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, XGBoost, and CatBoost — with **CatBoost Regressor** emerging as the best performer.

---

## Model Performance Comparison

| Model Name                | R² Score |
|----------------------------|----------|
| **CatBoost Regressor**     | **0.9793** |
| XGB Regressor              | 0.9787 |
| Random Forest Regressor    | 0.9771 |
| K-Neighbors Regressor      | 0.9721 |
| Decision Tree              | 0.9568 |
| Linear Regression          | 0.9373 |
| Ridge                      | 0.9373 |
| Lasso                      | 0.9372 |

**Final Model Used:** CatBoost Regressor  
    Model saved as: `1_final_model.pkl`

---

##  Features Used for Prediction

| Feature | Description |
|----------|-------------|
| **Carat** | Weight of the diamond |
| **Cut** | Quality of the cut (Fair, Good, Very Good, Premium, Ideal) |
| **Color** | Diamond color grade (J, I, H, G, F, E, D) |
| **Clarity** | Measure of how clear the diamond is (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF) |
| **Depth** | Total depth percentage |
| **Table** | Width of top of diamond relative to widest point |

---

##  Tech Stack

- **Python 3.12+**
- **CatBoost Regressor**
- **Scikit-learn**
- **Pandas, NumPy**
- **Matplotlib / Seaborn**
- **Streamlit** (for UI)
- **Joblib** (for model serialization)

---

---

##  How to Run Locally

### Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
---
## Create a Virtual Environment

```bash
python -m venv gemenv
gemenv\Scripts\activate     # for Windows
# source gemenv/bin/activate  # for macOS/Linux
```
---

## Install Dependencies

```bash
pip install -r requirements.txt
```
---

## Run Streamlit App

```bash
Run Streamlit App
```
---

