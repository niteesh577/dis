
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

if(add_selectbox == "Parkinsons Disease"):
     st.title('parkinsons disease prediction')

     fo=st.text_input('MDVP:Fo(Hz)')
     fhi=st.text_input('MDVP:Fhi(Hz)')
     flo=st.text_input('MDVP:Flo(Hz)')
     jitter=st.text_input('MDVP:Jitter(%)')
     Jitter=st.text_input('MDVP:Jitter(Abs)')
     RAP=st.text_input('MDVP:RAP')
     PPQ=st.text_input('PPQ')
     DDP=st.text_input('Jitter:DDP')
     Shimmer=st.text_input('MDVP:Shimmer')
     shimmer=st.text_input('MDVP:Shimmer(dB)')
     APQ3=st.text_input('Shimmer APQ3')
     APQ5=st.text_input('Shimmer APQ5')
     APQ=st.text_input('MDVP:APQ')
     DDA=st.text_input('Shimmer DDA')
     NHR=st.text_input('NHR')
     HNR=st.text_input('HNR')
     RPDE=st.text_input('RPDE')
     DFA=st.text_input('DFA')
     spread1=st.text_input('spread1')
     spread2=st.text_input('spread2')
     D2=st.text_input('D2')
     PPE=st.text_input('PPE')

     parks_diagnosis = ''
     if st.button('parkinsons test result'):
         parks_prediction = diabetes_model.predict(
             [[fo, fhi, flo, jitter, Jitter, RAP, PPQ, DDP,Shimmer,shimmer,APQ3,APQ5,APQ,DDA,NHR,RPDE,DFA,spread1,spread2,D2,PPE]])
         if (parks_prediction[0] == 1):
             parks_diagnosis = 'the person has parkinsons disease'
         else:
             parks_diagnosis = 'the person does not have parkinsons disease'
     st.success(parks_diagnosis)



if(add_selectbox == "Heart Disease"):
     st.title('heart disease prediction')

     age = st.text_input('age')
     sex = st.text_input('sex')
     cp = st.text_input('cp')
     trestbps = st.text_input('trestbps')
     chol = st.text_input('cholestrol')
     fbs = st.text_input('fbs')
     restecg = st.text_input('resrecq')
     thalach = st.text_input('thalach')
     exang = st.text_input('exang')
     oldpeak = st.text_input('oldpeak')
     slope = st.text_input('slope')
     ca = st.text_input('ca')
     thal = st.text_input('thal')

     heart_diagnosis = ''
     if st.button('Diagnosis test result'):
         heart_prediction = diabetes_model.predict(
             [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
         if (heart_prediction[0] == 1):
             heart_diagnosis = 'the person has heart disease'
         else:
             heart_diagnosis = 'the person does not have heart disease'
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