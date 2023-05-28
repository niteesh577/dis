
import pickle
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Which Disease you want to check with",
    ("Parkinsons Disease", "Heart Disease", "Diabetes"),

)
diabetes_model=pickle.load(open("diabetes_model.sav", 'rb'))
heartdis_model=pickle.load(open('heartdis_model.sav','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))

if add_selectbox == "Parkinsons Disease":
    st.title('Parkinsons Disease Prediction')

    fo_input = st.text_input('MDVP:Fo(Hz)')
    fhi_input = st.text_input('MDVP:Fhi(Hz)')
    flo_input = st.text_input('MDVP:Flo(Hz)')
    jitter_input = st.text_input('MDVP:Jitter(%)')
    Jitter_input = st.text_input('MDVP:Jitter(Abs)')
    RAP_input = st.text_input('MDVP:RAP')
    PPQ_input = st.text_input('PPQ')
    DDP_input = st.text_input('Jitter:DDP')
    Shimmer_input = st.text_input('MDVP:Shimmer')
    shimmer_input = st.text_input('MDVP:Shimmer(dB)')
    APQ3_input = st.text_input('Shimmer APQ3')
    APQ5_input = st.text_input('Shimmer APQ5')
    APQ_input = st.text_input('MDVP:APQ')
    DDA_input = st.text_input('Shimmer DDA')
    NHR_input = st.text_input('NHR')
    HNR_input = st.text_input('HNR')
    RPDE_input = st.text_input('RPDE')
    DFA_input = st.text_input('DFA')
    spread1_input = st.text_input('spread1')
    spread2_input = st.text_input('spread2')
    D2_input = st.text_input('D2')
    PPE_input = st.text_input('PPE')

    parks_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        if (
            fo_input
            and fhi_input
            and flo_input
            and jitter_input
            and Jitter_input
            and RAP_input
            and PPQ_input
            and DDP_input
            and Shimmer_input
            and shimmer_input
            and APQ3_input
            and APQ5_input
            and APQ_input
            and DDA_input
            and NHR_input
            and HNR_input
            and RPDE_input
            and DFA_input
            and spread1_input
            and spread2_input
            and D2_input
            and PPE_input
        ):
            fo = float(fo_input)
            fhi = float(fhi_input)
            flo = float(flo_input)
            jitter = float(jitter_input)
            Jitter = float(Jitter_input)
            RAP = float(RAP_input)
            PPQ = float(PPQ_input)
            DDP = float(DDP_input)
            Shimmer = float(Shimmer_input)
            shimmer = float(shimmer_input)
            APQ3 = float(APQ3_input)
            APQ5 = float(APQ5_input)
            APQ = float(APQ_input)
            DDA = float(DDA_input)
            NHR = float(NHR_input)
            HNR = float(HNR_input)
            RPDE = float(RPDE_input)
            DFA = float(DFA_input)
            spread1 = float(spread1_input)
            spread2 = float(spread2_input)
            D2 = float(D2_input)
            PPE = float(PPE_input)

            parks_prediction





if add_selectbox == "Heart Disease":
    st.title('Heart Disease Prediction')

    age = None
    try:
        age = float(st.text_input('Age'))
    except ValueError:
        pass

    sex = None
    try:
        sex = float(st.text_input('Sex'))
    except ValueError:
        pass

    cp = None
    try:
        cp = float(st.text_input('Chest Pain Type (cp)'))
    except ValueError:
        pass

    trestbps = None
    try:
        trestbps = float(st.text_input('Resting Blood Pressure (trestbps)'))
    except ValueError:
        pass

    chol = None
    try:
        chol = float(st.text_input('Cholesterol (chol)'))
    except ValueError:
        pass

    fbs = None
    try:
        fbs = float(st.text_input('Fasting Blood Sugar (fbs)'))
    except ValueError:
        pass

    restecg = None
    try:
        restecg = float(st.text_input('Resting Electrocardiographic Results (restecg)'))
    except ValueError:
        pass

    thalach = None
    try:
        thalach = float(st.text_input('Maximum Heart Rate Achieved (thalach)'))
    except ValueError:
        pass

    exang = None
    try:
        exang = float(st.text_input('Exercise Induced Angina (exang)'))
    except ValueError:
        pass

    oldpeak = None
    try:
        oldpeak = float(st.text_input('ST Depression Induced by Exercise Relative to Rest (oldpeak)'))
    except ValueError:
        pass

    slope = None
    try:
        slope = float(st.text_input('Slope of the ST Segment (slope)'))
    except ValueError:
        pass

    ca = None
    try:
        ca = float(st.text_input('Number of Major Vessels (0-3) Colored by Fluoroscopy (ca)'))
    except ValueError:
        pass

    thal = None
    try:
        thal = float(st.text_input('Thalassemia (thal)'))
    except ValueError:
        pass

    heart_diagnosis = ''
    if st.button('Diagnosis Test Result'):
        if (
            age is not None and sex is not None and cp is not None and trestbps is not None and chol is not None
            and fbs is not None and restecg is not None and thalach is not None and exang is not None
            and oldpeak is not None and slope is not None and ca is not None and thal is not None
        ):
            heart_prediction = heartdis_model.predict(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            )
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease.'
            else:
                heart_diagnosis = 'The person does not have heart disease.'
        else:
            heart_diagnosis = 'Please provide valid input for all fields.'
    st.success(heart_diagnosis)





if(add_selectbox == "Diabetes"):
     st.title('Diabetes prediction')

     Pregnancies = st.text_input('number of Pregnancies')
     Glucose = st.text_input('Glucose level')
     BloodPressure = st.text_input('Blood Pressure value')
     SkinThickness = st.text_input('skin Thickness value')
     Insulin = st.text_input('Insulin level')
     BMI = st.text_input('BMI value')
     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
     Age = st.text_input('Age of the Person')

     diab_diagnosis= ''
     if st.button('Diagnosis test result'):
         diab_prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
         if(diab_prediction[0]==1):
             diab_diagnosis='the person is Diabetic'
         else:
             diab_diagnosis='the person is not Diabetic'
     st.success(diab_diagnosis)
