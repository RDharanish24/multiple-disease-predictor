import pickle
from streamlit_option_menu import option_menu
import streamlit as st

# Load models
import pickle

# Load Diabetics Model
with open(r"C:\Users\DELL\Documents\ml projects\multiple disease predictor\models\trained_model.sav", 'rb') as file:
    diabetics_model = pickle.load(file)

# Load Breast Cancer Model
with open(r"C:\Users\DELL\Documents\ml projects\multiple disease predictor\models\breastcancermodel.sav", 'rb') as file:
    breastcancer_model = pickle.load(file)

# Load Heart Disease Model
with open(r"C:\Users\DELL\Documents\ml projects\multiple disease predictor\models\heartdiseasemodel.sav", 'rb') as file:
    heartdisease_model = pickle.load(file)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetics Prediction", "Heart Disease Prediction",
            "Breast Cancer Prediction"],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Page display
if selected == "Diabetics Prediction":
    st.title("Diabetics Prediction")
    Pregnancies = st.text_input("pregnancies")
    Glucose = st.text_input("glucose")
    BloodPressure = st.text_input("bloodpressure")
    SkinThickness = st.text_input("skinthickness")
    Insulin = st.text_input("insulin")
    BMI = st.text_input("bmi")
    DiabetesPedigreeFunction = st.text_input("DPF")
    Age = st.text_input("age")

    dia_inp = ''

    if st.button("diabetics result"):
        dia_pre = diabetics_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (dia_pre[0] == 1):
            dia_inp = 'the person is diabetic'
        else:
            dia_inp = 'the person is not diabetic'
    st.success(dia_inp)

elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    
    age = st.number_input("Enter Age", min_value=1, max_value=120, step=1)
    sex = st.number_input("Enter Sex (1 = Male, 0 = Female)", min_value=0, max_value=1, step=1)
    cp = st.number_input("Enter Chest Pain Type (0-3)", min_value=0, max_value=3, step=1)
    trestbps = st.number_input("Enter Resting Blood Pressure (trestbps)", min_value=50, max_value=250, step=1)
    chol = st.number_input("Enter Serum Cholestoral (chol)", min_value=100, max_value=600, step=1)
    fbs = st.number_input("Enter Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", min_value=0, max_value=1, step=1)
    restecg = st.number_input("Enter Resting Electrocardiographic Results (0-2)", min_value=0, max_value=2, step=1)
    thalach = st.number_input("Enter Maximum Heart Rate Achieved (thalach)", min_value=50, max_value=250, step=1)
    exang = st.number_input("Enter Exercise Induced Angina (1 = Yes, 0 = No)", min_value=0, max_value=1, step=1)
    oldpeak = st.number_input("Enter ST Depression Induced by Exercise (oldpeak)", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
    slope = st.number_input("Enter Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2, step=1)
    ca = st.number_input("Enter Number of Major Vessels Colored by Fluoroscopy (0-4)", min_value=0, max_value=4, step=1)
    thal = st.number_input("Enter Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)", min_value=0, max_value=3, step=1)

    
    heart_inp = ''

    if st.button("Heart Disease Result"):
        heart_pre = heartdisease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
              exang, oldpeak, slope, ca, thal]]
        )
    
        if (heart_pre[0] == 1):
            heart_inp = 'The person has heart disease'
        else:
            heart_inp = 'The person does not have heart disease'
    
    st.success(heart_inp)


  
    
elif selected == "Breast Cancer Prediction":
    st.title("Breast Cancer Prediction")
    radius = st.text_input("Enter Mean Radius")
    texture = st.text_input("Enter Mean Texture")
    perimeter = st.text_input("Enter Mean Perimeter")
    area = st.text_input("Enter Mean Area")
    mean_smoothness = st.text_input("Enter Mean Smoothness")
    mean_compactness = st.text_input("Enter Mean Compactness")
    mean_concavity = st.text_input("Enter Mean Concavity")
    mean_concave_points = st.text_input("Enter Mean Concave Points")
    mean_symmetry = st.text_input("Enter Mean Symmetry")
    mean_fractal_dimension = st.text_input("Enter Mean Fractal Dimension")
    
    radius_error = st.text_input("Enter Radius Error")
    texture_error = st.text_input("Enter Texture Error")
    perimeter_error = st.text_input("Enter Perimeter Error")
    area_error = st.text_input("Enter Area Error")
    smoothness_error = st.text_input("Enter Smoothness Error")
    compactness_error = st.text_input("Enter Compactness Error")
    concavity_error = st.text_input("Enter Concavity Error")
    concave_points_error = st.text_input("Enter Concave Points Error")
    symmetry_error = st.text_input("Enter Symmetry Error")
    fractal_dimension_error = st.text_input("Enter Fractal Dimension Error")
    
    worst_radius = st.text_input("Enter Worst Radius")
    worst_texture = st.text_input("Enter Worst Texture")
    worst_perimeter = st.text_input("Enter Worst Perimeter")
    worst_area = st.text_input("Enter Worst Area")
    worst_smoothness = st.text_input("Enter Worst Smoothness")
    worst_compactness = st.text_input("Enter Worst Compactness")
    worst_concavity = st.text_input("Enter Worst Concavity")
    worst_concave_points = st.text_input("Enter Worst Concave Points")
    worst_symmetry = st.text_input("Enter Worst Symmetry")
    worst_fractal_dimension = st.text_input("Enter Worst Fractal Dimension")


   

    
    heart_inp = ''

    if st.button("heart disease result"):
        heart_pre = heartdisease_model.predict(
            [[radius, texture, perimeter, area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension
]])
        if (heart_pre[0] == 1):
            heart_inp = 'the person has heart disease'
        else:
            heart_inp = 'the person is not diabetic'
    st.success(heart_inp)

