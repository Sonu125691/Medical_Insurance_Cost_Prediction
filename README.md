# 🏥 Medical Insurance Cost Prediction

An end-to-end Machine Learning regression project that predicts medical insurance costs using demographic and lifestyle factors.  
The project covers EDA, data preprocessing, model comparison, evaluation, and deployment using Streamlit.

---

## 📌 Problem Statement

Medical insurance costs vary significantly based on demographic and lifestyle factors such as age, sex, BMI, number of children, smoking status, and region.
This project aims to develop a regression model for predicting insurance charges and present the model through an interactive Streamlit user interface for easy usage.

---

## Dataset

- Total records: **1338**
- Target variable: **charges**(Medical Insurance Cost)

**Note:** The dataset is **U.S.-based**, and the `region` feature corresponds to U.S. geographic regions.

### Features
- `age` – Age of the individual
- `sex` – Gender
- `bmi` – Body Mass Index
- `children` – Number of children
- `smoker` – Smoking status
- `region` – Residential region (U.S.-based: southwest, northwest, northeast, southeast)

---

## Project Workflow

### 1. Train-Test Split
- The dataset was split into training and testing sets.
- Exploratory Data Analysis (EDA) was performed **only on training data** to avoid data leakage.

---

### 2. Exploratory Data Analysis (EDA)
- Distribution analysis of numerical features
- Relationship between features and insurance charges

---

### 3. Data Preprocessing
- Binary categorical values (**yes/no**) were manually converted into numerical format
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
- The trained model, along with the scaler and encoder, was saved using **pickle** for use within the Streamlit application

---

## Streamlit User Interface
- An interactive Streamlit-based user interface was developed
- Users can easily input feature values and receive predicted medical insurance costs

---

## Tech Stack
- **Programming Language:** Python
- **Libraries & Tools:**
  - Pandas
  - Scikit-learn
  - XGBoost
  - Matplotlib
  - Seaborn
  - Streamlit
