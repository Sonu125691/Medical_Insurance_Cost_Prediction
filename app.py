import pickle 
import streamlit as st
import pandas as pd


with open("encoder.pkl", "rb") as file:
    encoder = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


st.title("Medical Insurance Cost Prediction")
st.subheader("This application will predicts the Medical insurance cost. Please provide the required details.")

age = st.slider("Age", 18, 110, 18)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI(Body Mass Index)", min_value = 5.000, max_value = 100.000, step = 0.001)
children = st.number_input("Number of Children", min_value = 0, max_value = 20)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["North East", "North West", "South East", "South West"])

sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

region = region.lower().replace(" ", "")

user_input = {
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children,
    "smoker": smoker,
    "region": region
}

input = pd.DataFrame([user_input])

if st.button("Predict"):
    encoding = encoder.transform(input[["region"]])
    encoded = pd.DataFrame(encoding, columns = encoder.get_feature_names_out(["region"]))

    input = input.drop(columns = ["region"])
    input = pd.concat([input, encoded], axis = 1)

    input = scaler.transform(input)

    prediction = model.predict(input)

    st.success(f"Medical Insurance Cost is $ {prediction[0]:.3f}")