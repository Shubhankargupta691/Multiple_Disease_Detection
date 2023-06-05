import pickle
import streamlit as st

# Load the models
diabetes_model = pickle.load(open('./saved models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('./saved models/heart_disease_model.sav', 'rb'))
kidney_model = pickle.load(open('./saved models/kidney_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('./saved models/parkinsons_model.sav', 'rb'))

# Disease options
disease_options = ["Diabetes", "Heart Disease", "Kidney Disease", "Parkinson's"]

# Page title and disease selection
st.title("Multiple Disease Prediction")
selected_disease = st.selectbox("Select the disease", disease_options)

# Function to convert input values to the appropriate data type
def convert_input(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

# Disease prediction logic
if selected_disease == "Diabetes":
    st.title(f"You have selected {selected_disease}")

    # Get input data from the user
    pregnancies = st.text_input('Number of Pregnancies')
    glucose = st.text_input('Glucose Level')
    blood_pressure = st.text_input('Blood Pressure value')
    skin_thickness = st.text_input('Skin Thickness value')
    insulin = st.text_input('Insulin Level')
    bmi = st.text_input('BMI value')
    diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value')
    age = st.text_input('Age of the Person')

    # Code for prediction
    if st.button('Diabetes Test Result'):
        input_data = [convert_input(pregnancies), convert_input(glucose), convert_input(blood_pressure),
                      convert_input(skin_thickness), convert_input(insulin), convert_input(bmi),
                      convert_input(diabetes_pedigree_function), convert_input(age)]
        diab_prediction = diabetes_model.predict([input_data])[0]
        diab_diagnosis = 'The person is diabetic' if diab_prediction == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

elif selected_disease == "Heart Disease":
    st.title(f"You have selected {selected_disease}")

    # Get input data from the user
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholesterol in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Number of Major vessels colored by fluoroscopy')
    thal = st.text_input('Thal: 0 = normal, 1 = fixed defect, 2 = reversable defect')

    # Code for prediction
    if st.button('Heart Disease Test Result'):
        input_data = [convert_input(age), convert_input(sex), convert_input(cp), convert_input(trestbps),
                      convert_input(chol), convert_input(fbs), convert_input(restecg), convert_input(thalach),
                      convert_input(exang), convert_input(oldpeak), convert_input(slope), convert_input(ca),
                      convert_input(thal)]
        heart_prediction = heart_model.predict([input_data])[0]
        heart_diagnosis = 'The person is having heart disease' if heart_prediction == 1 else 'The person does not have any heart disease'
        st.success(heart_diagnosis)

elif selected_disease == "Parkinson's":
    st.title(f"You have selected {selected_disease}")

    # Get input data from the user
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    jitter_percent = st.text_input('MDVP:Jitter(%)')
    jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    rap = st.text_input('MDVP:RAP')
    ppq = st.text_input('MDVP:PPQ')
    ddp = st.text_input('Jitter:DDP')
    shimmer = st.text_input('MDVP:Shimmer')
    shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    apq3 = st.text_input('Shimmer:APQ3')
    apq5 = st.text_input('Shimmer:APQ5')
    apq = st.text_input('MDVP:APQ')
    dda = st.text_input('Shimmer:DDA')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    rpde = st.text_input('RPDE')
    dfa = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    d2 = st.text_input('D2')
    ppe = st.text_input('PPE')

    # Code for prediction
    if st.button("Parkinson's Test Result"):
        input_data = [convert_input(fo), convert_input(fhi), convert_input(flo), convert_input(jitter_percent),
                      convert_input(jitter_abs), convert_input(rap), convert_input(ppq), convert_input(ddp),
                      convert_input(shimmer), convert_input(shimmer_db), convert_input(apq3), convert_input(apq5),
                      convert_input(apq), convert_input(dda), convert_input(nhr), convert_input(hnr),
                      convert_input(rpde), convert_input(dfa), convert_input(spread1), convert_input(spread2),
                      convert_input(d2), convert_input(ppe)]
        parkinsons_prediction = parkinsons_model.predict([input_data])[0]
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)

elif selected_disease == "Kidney Disease":
    st.title(f"You have selected {selected_disease}")

    # Get input data from the user
    age = st.text_input('Age')
    bp = st.text_input('Blood Pressure')
    sg = st.text_input('Specific Gravity')
    al = st.text_input('Albumin')
    su = st.text_input('Sugar')
    rbc = st.text_input('Red Blood Cells')
    pc = st.text_input('Pus Cell')
    pcc = st.text_input('Pus Cell Clumps')
    ba = st.text_input('Bacteria')
    bgr = st.text_input('Blood Glucose Random')
    bu = st.text_input('Blood Urea')
    sc = st.text_input('Serum Creatinine')
    sod = st.text_input('Sodium')
    pot = st.text_input('Potassium')
    hemo = st.text_input('Hemoglobin')
    pcv = st.text_input('Packed Cell Volume')
    wc = st.text_input('White Blood Cell Count')
    rc = st.text_input('Red Blood Cell Count')
    htn = st.text_input('Hypertension')
    dm = st.text_input('Diabetes Mellitus')
    cad = st.text_input('Coronary Artery Disease')
    appet = st.text_input('Appetite')
    pe = st.text_input('Pedal Edema')
    ane = st.text_input('Anemia')

    # Code for prediction
    if st.button('Kidney Disease Test Result'):
        input_data = [convert_input(age), convert_input(bp), convert_input(sg), convert_input(al), convert_input(su),
                      convert_input(rbc), convert_input(pc), convert_input(pcc), convert_input(ba), convert_input(bgr),
                      convert_input(bu), convert_input(sc), convert_input(sod), convert_input(pot), convert_input(hemo),
                      convert_input(pcv), convert_input(wc), convert_input(rc), convert_input(htn), convert_input(dm),
                      convert_input(cad), convert_input(appet), convert_input(pe), convert_input(ane)]
        kidney_prediction = kidney_model.predict([input_data])[0]
        kidney_diagnosis = 'The person has kidney disease' if kidney_prediction == 1 else 'The person does not have kidney disease'
        st.success(kidney_diagnosis)
