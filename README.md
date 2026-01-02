# 🏥Medical Insurance Cost Prediction

An end-to-end Machine Learning regression project that predicts medical insurance costs using demographic and lifestyle factors.  
The project covers data preprocessing, model comparison, evaluation, and deployment using Streamlit.

---

📌 Problem Statement

Medical insurance costs vary significantly based on demographic and lifestyle factors such as age, sex, BMI, number of children, smoking status, and region.
This project aims to develop a regression model for predicting insurance charges and present the model through an interactive Streamlit user interface for easy usage.

## Dataset

- Total records: **1338**
- Target variable: **charges**

### Features
- `age` – Age of the individual
- `sex` – Gender
- `bmi` – Body Mass Index
- `children` – Number of children
- `smoker` – Smoking status
- `region` – Residential region (4 unique categories)

---

## Project Workflow

### 1. Train-Test Split
- The dataset was split into training and testing sets.
- Exploratory Data Analysis (EDA) was performed **only on training data** to avoid data leakage.

---

### 2. Exploratory Data Analysis (EDA)
- Distribution analysis of numerical features
- Relationship between features and insurance charges
- Detection of patterns and potential outliers

---

### 3. Data Preprocessing
- **One-Hot Encoding**
  - Applied to the `region` column since it is categorical with 4 unique values
- **Standard Scaling**
  - Applied to numerical features to normalize feature ranges

---

### 4. Model Training
The following regression models were trained and evaluated:

- Linear Regression
- Support Vector Regressor (SVR)
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

For each model:
- Hyperparameters were tuned manually
- Models were evaluated using R² score, Mean Squared Error, and Mean Absolute Error

---

### 5. Model Evaluation

After comparing all models, **XGBoost Regressor** achieved the best performance.

#### XGBoost Performance Metrics
- **R² Score (Train):** 0.8844494835322138
- **R² Score (Test):** 0.8634147863642154
- **Mean Squared Error (Test):** 15733734.744721843
- **Mean Absolute Error (Test):** 2349.8365586833024

---

### 6. Final Model
- XGBoost Regressor was selected as the final model
- The model was retrained on the **full dataset** using the same optimized hyperparameters
- The trained model was saved for deployment

---

## Streamlit Web Application
- An interactive Streamlit application was developed
- Users can input feature values and receive predicted medical insurance costs
- Enables real-time prediction through a web interface

---

## Tech Stack
- **Programming Language:** Python
- **Libraries & Tools:**
  - NumPy
  - Pandas
  - Scikit-learn
  - XGBoost
  - Matplotlib
  - Seaborn
  - Streamlit

---

## How to Run the Project

```bash
git clone https://github.com/your-username/Medical_Insurance_Cost_Prediction.git
cd Medical_Insurance_Cost_Prediction
pip install -r requirements.txt
streamlit run app.py
