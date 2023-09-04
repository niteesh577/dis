




# new
import streamlit as st

# Home Page
def home():
    st.title("Home Page")

    st.markdown("""
 Vocal biomarkers are acoustic features that can be extracted from speech signals. These features can be used to identify and diagnose a variety of medical conditions, including Parkinson's disease, Alzheimer's disease, and depression.

 Vocal biomarkers are extracted using a variety of methods, including:

 * Time-domain analysis: This involves analyzing the time-varying characteristics of the speech signal, such as the fundamental frequency (F0), the amplitude, and the duration of the signal.
 * Frequency-domain analysis: This involves analyzing the frequency components of the speech signal, such as the spectral centroid, the spectral slope, and the spectral entropy.
 * Time-frequency analysis: This involves analyzing the time-frequency characteristics of the speech signal, such as the wavelet transform and the short-time Fourier transform.

 The choice of method depends on the specific vocal biomarker that is being extracted and the medical condition that is being diagnosed.

 Vocal biomarkers have been shown to be effective in detecting and diagnosing a variety of medical conditions. For example, a study published in the journal Neurology found that vocal biomarkers could be used to diagnose Parkinson's disease with 90% accuracy.

 Vocal biomarkers are a promising new tool for early diagnosis and treatment of medical conditions. As research in this area continues, it is likely that vocal biomarkers will become even more accurate and reliable.

 Here are some of the benefits of using vocal biomarkers:

 * They are non-invasive and can be easily collected.
 * They can be used to monitor the progression of a disease over time.
 * They can be used to assess the effectiveness of treatment.

 However, there are also some challenges associated with using vocal biomarkers:

 * The accuracy of vocal biomarkers can vary depending on the specific condition being diagnosed.
 * Vocal biomarkers can be affected by a variety of factors, such as the speaker's age, gender, and emotional state.
 """)




# About Page
def about():
    st.title("About the various diseases")

    # Main content
    st.markdown("## Alzheimer's Disease")
    st.markdown(
        "Alzheimer's disease is a progressive neurological disorder that affects the brain and impairs memory, thinking, and behavior. It is the most common form of dementia, accounting for around 60-80% of all dementia cases. Alzheimer's disease typically occurs in older adults, although it can also affect younger individuals.")
    st.markdown(
        "The exact cause of Alzheimers disease is not fully understood, but it is believed to be a combination of genetic, lifestyle, and environmental factors. The hallmark characteristics of Alzheimers disease are the accumulation of abnormal protein deposits called amyloid plaques and tau tangles in the brain. These deposits disrupt the normal functioning of brain cells and lead to their degeneration and eventual death.")
    st.markdown(
        "The progression of Alzheimers disease is gradual, and the symptoms worsen over time. Early symptoms may include mild memory loss and difficulties with language, reasoning, and problem-solving. As the disease advances, individuals may experience confusion, disorientation, changes in mood and behavior, difficulty speaking and swallowing, and a decline in overall cognitive function.")
    st.markdown(
        "Currently, there is no cure for Alzheimer's disease, but there are treatments available that can help manage symptoms and improve quality of life. These treatments may include medications to alleviate cognitive and behavioral symptoms, as well as non-drug approaches such as cognitive training and support for caregivers.")
    st.markdown(
        "Research into Alzheimer's disease is ongoing, with scientists working to better understand its causes and develop new interventions. Early detection and diagnosis are crucial for managing the disease effectively and providing appropriate support and care to individuals and their families affected by Alzheimer's disease.")

    st.markdown("## Parkinson's Disease")
    st.markdown(
        "Parkinson's disease is a neurodegenerative disorder that primarily affects the motor system. It is characterized by a loss of dopamine-producing cells in a specific region of the brain called the substantia nigra. Dopamine is a neurotransmitter that plays a crucial role in coordinating movement, and its deficiency leads to the motor symptoms associated with Parkinson's disease.")
    st.markdown(
        "The exact cause of Parkinson's disease is not fully understood, but it is believed to involve a combination of genetic and environmental factors. The majority of cases are considered idiopathic, meaning the cause is unknown. However, certain genetic mutations and environmental factors, such as exposure to toxins, have been identified as potential risk factors.")
    st.markdown(
        "The primary symptoms of Parkinson's disease include tremors (uncontrollable shaking), rigidity (stiffness of muscles), bradykinesia (slowness of movement), and postural instability (difficulty maintaining balance). These motor symptoms can vary in severity and may progress over time. Other non-motor symptoms may also occur, such as cognitive impairment, depression, sleep disturbances, and autonomic dysfunction.")
    st.markdown(
        "Although there is currently no cure for Parkinson's disease, there are treatments available to manage its symptoms and improve quality of life. Medications can help increase dopamine levels or mimic its effects in the brain, providing relief from motor symptoms. In advanced cases, deep brain stimulation (DBS) surgery may be considered to implant electrodes in specific brain regions to alleviate symptoms.")
    st.markdown(
        "In addition to medical treatments, physical therapy, occupational therapy, and speech therapy can be beneficial in managing the physical and functional challenges associated with Parkinson's disease. Lifestyle modifications, such as regular exercise, a balanced diet, and stress management, may also have a positive impact on symptom management and overall well-being.")
    st.markdown(
        "Research into Parkinson's disease is ongoing, with scientists working to better understand its underlying mechanisms and develop new therapies. Early diagnosis and comprehensive treatment planning, including a multidisciplinary approach involving healthcare professionals, can help individuals with Parkinson's disease effectively manage their symptoms and maintain an optimal quality of life.")

    st.markdown("## Dementia")
    st.markdown(
        "Dementia is a syndrome characterized by a decline in cognitive function and other abilities that interfere with daily functioning. It is not a specific disease but rather a group of symptoms that affect memory, thinking, behavior, and the ability to perform everyday activities. Dementia is usually caused by damage or disease in the brain, most commonly seen in older adults.")
    st.markdown(
        "The most common type of dementia is Alzheimer's disease, accounting for approximately 60-70% of cases. Alzheimer's disease is characterized by the accumulation of abnormal protein deposits in the brain, leading to the progressive loss of brain cells and the deterioration of cognitive function.")
    st.markdown(
        "Other types of dementia include vascular dementia, which is caused by reduced blood flow to the brain due to stroke or other vascular conditions, and Lewy body dementia, which is characterized by the presence of abnormal protein deposits called Lewy bodies in the brain. There are also several less common types of dementia, such as frontotemporal dementia and Parkinson's disease dementia.")
    st.markdown(
        "The symptoms of dementia vary depending on the type and stage of the condition but commonly include memory loss, confusion, difficulty with language and communication, impaired judgment, personality changes, and problems with daily tasks. As dementia progresses, individuals may experience difficulties with mobility, coordination, and self-care.")
    st.markdown(
        "The impact of dementia on individuals and their families can be significant. It requires specialized care and support to manage the symptoms, ensure safety, and maintain quality of life. Treatment for dementia aims to alleviate symptoms, slow down the progression of the disease, and provide support for both the individual and their caregivers.")
    st.markdown(
        "While there is currently no cure for most types of dementia, early diagnosis and interventions can help manage symptoms and improve quality of life. Medications may be prescribed to manage cognitive symptoms and address associated conditions, such as depression or sleep disturbances. Non-pharmacological interventions, such as cognitive stimulation therapy, physical exercise, and social engagement, can also be beneficial.")
    st.markdown(
        "Support from healthcare professionals, dementia care services, and community resources is crucial for individuals with dementia and their caregivers. Education, counseling, and support groups can provide valuable information and emotional support to navigate the challenges of living with dementia.")
    st.markdown(
        "Research into understanding the causes, prevention, and treatment of dementia is ongoing. Efforts are focused on finding ways to delay the onset of dementia, identify biomarkers for early detection, and develop new therapies. Promoting brain health through a healthy lifestyle, including regular exercise, a balanced diet, mental stimulation, and social engagement, is also considered important for reducing the risk of dementia.")

    st.markdown("## Depression")
    st.markdown(
        "Depression, also known as major depressive disorder, is a common and serious mental health condition characterized by persistent feelings of sadness, loss of interest or pleasure in activities, and a range of physical and emotional symptoms. It affects how a person thinks, feels, and functions, and can interfere with their daily life.")

    st.markdown(
        "The exact cause of depression is not known, but it is believed to result from a combination of genetic, biological, environmental, and psychological factors. Certain life events, such as trauma, loss, or chronic stress, can increase the risk of developing depression. Additionally, imbalances in brain chemicals called neurotransmitters, such as serotonin and norepinephrine, are thought to play a role in the development of depression.")

    st.markdown("Symptoms of depression can vary in severity and duration but commonly include:")

    st.markdown("1. Persistent feelings of sadness, emptiness, or hopelessness.")
    st.markdown("2. Loss of interest or pleasure in activities once enjoyed.")
    st.markdown("3. Changes in appetite and weight (either significant weight loss or gain).")
    st.markdown("4. Sleep disturbances, such as insomnia or excessive sleep.")
    st.markdown("5. Fatigue or loss of energy.")
    st.markdown("6. Feelings of worthlessness or excessive guilt.")
    st.markdown("7. Difficulty concentrating, making decisions, or remembering things.")
    st.markdown("8. Restlessness or slowed movements.")
    st.markdown("9. Physical symptoms such as headaches, stomachaches, or back pain.")
    st.markdown("10. Thoughts of death or suicide.")
    st.markdown(
        "It's important to note that experiencing some of these symptoms for a short period doesn't necessarily mean a person has depression. However, if these symptoms persist for at least two weeks and significantly impact daily functioning and well-being, it may be indicative of a depressive episode.")

    st.markdown(
        "Depression is a treatable condition, and various approaches can be effective in managing and alleviating symptoms. Treatment may involve a combination of psychotherapy (talk therapy), medication (such as antidepressants), and lifestyle changes. Psychotherapy can help individuals explore their thoughts, emotions, and behaviors, develop coping strategies, and improve problem-solving skills. Antidepressant medications work by balancing brain chemicals and can be prescribed by a healthcare professional. Additionally, making positive lifestyle changes such as engaging in regular exercise, practicing stress-reducing techniques (e.g., mindfulness or meditation), maintaining a healthy diet, and seeking support from loved ones can also contribute to improving mood and overall well-being.")

    st.markdown(
        "It's crucial for individuals experiencing symptoms of depression to seek professional help. A mental health professional, such as a psychiatrist, psychologist, or licensed therapist, can provide an accurate diagnosis and develop an appropriate treatment plan. With the right support and treatment, individuals with depression can experience significant improvement in their symptoms and regain a sense of well-being and quality of life.")


# Disease Detection Page
def disease_detection():
    import streamlit as st
    st.header("Disease Detection Page")
    add_selectbox = st.sidebar.selectbox(
        "Which Disease you want to check with",
        ("Parkinsons Disease", "Heart Disease", "Diabetes"),

    )
    import pickle
    diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
    heartdis_model = pickle.load(open('heartdis_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

    if add_selectbox == "Parkinsons Disease":

        import pickle
        import streamlit as st
        import numpy as np
        import sounddevice as sd
        import librosa
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import SVC
        from sklearn import svm

        # Load the trained model
        parkinsons_model = svm.SVC(kernel='linear')

        def record_audio(duration):
            fs = 44100  # Sample rate
            sd.default.samplerate = fs
            sd.default.channels = 1  # Mono audio
            audio_data = sd.rec(int(duration * fs))
            sd.wait()  # Wait until recording is finished
            return audio_data.flatten()

        def extract_features(audio_data):
            # Reshape audio data to 2D array with shape (n_samples, n_channels)
            audio_data = audio_data.reshape(-1, 1)

            # Compute spectrogram
            spectrogram = np.abs(librosa.stft(audio_data).T)

            # Adjust the number of octaves to match your data
            num_octaves = 3
            fo = librosa.feature.zero_crossing_rate(audio_data).mean()
            fhi = librosa.feature.spectral_centroid(S=spectrogram).mean()
            flo = librosa.feature.spectral_contrast(S=spectrogram).mean()
            jitter = librosa.feature.rms(y=audio_data).mean()
            Jitter = librosa.feature.tonnetz(y=audio_data, sr=44100).mean()
            RAP = librosa.feature.mfcc(y=audio_data, sr=44100, n_mfcc=20).mean()
            PPQ = librosa.feature.chroma_stft(y=audio_data, sr=44100).mean()
            DDP = librosa.feature.rms(y=audio_data).mean()
            Shimmer = librosa.feature.spectral_bandwidth(y=audio_data).mean()
            shimmer = librosa.feature.spectral_rolloff(y=audio_data).mean()
            APQ3 = librosa.feature.spectral_flatness(y=audio_data).mean()
            APQ5 = librosa.feature.melspectrogram(y=audio_data, sr=44100).mean()
            APQ = librosa.feature.tempogram(y=audio_data, sr=44100).mean()
            DDA = librosa.feature.poly_features(y=audio_data).mean()
            NHR = librosa.feature.tonnetz(y=audio_data, sr=44100).mean()
            HNR = librosa.feature.zero_crossing_rate(y=audio_data).mean()
            RPDE = librosa.feature.spectral_contrast(y=audio_data).mean()
            DFA = librosa.feature.tonnetz(y=audio_data, sr=44100).mean()
            spread1 = librosa.feature.spectral_bandwidth(y=audio_data).mean()
            spread2 = librosa.feature.spectral_contrast(y=audio_data).mean()
            D2 = librosa.feature.chroma_cqt(y=audio_data, sr=44100, n_chroma=12, n_octaves=num_octaves).mean()
            PPE = librosa.feature.spectral_contrast(y=audio_data).mean()

            features = [fo, fhi, flo, jitter, Jitter, RAP, PPQ, DDP, Shimmer, shimmer, APQ3, APQ5, APQ, DDA, NHR, HNR,
                        RPDE, DFA, spread1, spread2, D2, PPE]

            return features

        # Streamlit app
        st.title("Parkinson's Disease Prediction")

        # Record and predict
        duration = st.slider("Recording Duration (seconds)", min_value=1, max_value=40, value=3)
        if st.button("Start Recording"):
            st.write("Recording...")
            audio_data = record_audio(duration)
            st.write("Recording finished!")

            # Define segment duration and overlap
            segment_duration = 5  # Length of each segment in seconds
            overlap_duration = 2  # Length of overlap between segments in seconds

            # Initialize a list to store predictions for each segment
            segment_predictions = []

            # Process audio segments sequentially
            start = 0
            end = start + segment_duration

            while end <= len(audio_data):
                segment = audio_data[start:end]

                # Extract features from the segment
                features = extract_features(segment)

                # Scale the features using StandardScaler
                scaler = StandardScaler()
                scaled_features = scaler.transform(np.array(features).reshape(1, -1))

                # Make prediction using the trained model
                segment_prediction = parkinsons_model.predict(scaled_features)

                # Store the prediction for this segment
                segment_predictions.append(segment_prediction[0])

                # Move to the next segment with overlap
                start += segment_duration - overlap_duration
                end = start + segment_duration

            # Determine the final prediction based on the segments
            final_prediction = 1 if sum(segment_predictions) > len(segment_predictions) / 2 else 0

            if final_prediction == 1:
                parks_diagnosis = "The person has Parkinson's disease."
            else:
                parks_diagnosis = "The person does not have Parkinson's disease."

                st.success(parks_diagnosis)
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

    if (add_selectbox == "Diabetes"):
        st.title('Diabetes prediction')

        Pregnancies = st.text_input('number of Pregnancies')
        Glucose = st.text_input('Glucose level')
        BloodPressure = st.text_input('Blood Pressure value')
        SkinThickness = st.text_input('skin Thickness value')
        Insulin = st.text_input('Insulin level')
        BMI = st.text_input('BMI value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        Age = st.text_input('Age of the Person')

        diab_diagnosis = ''
        if st.button('Diagnosis test result'):
            diab_prediction = diabetes_model.predict(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'the person is Diabetic'
            else:
                diab_diagnosis = 'the person is not Diabetic'
        st.success(diab_diagnosis)


# Contact Page
def contact():
    st.title("Contact Page")
    st.markdown("""
        # Contact the Doctor

        Information about contacting the doctor...
        """)

# Blogs Page
def blogs():
    st.title("Blogs Page")
    st.write("Welcome to the Blogs Page!")

# Sidebar Navigation
nav_selection = st.sidebar.radio("Navigation", ("Home", "About", "Disease Detection", "Contact", "Blogs"))

# Page Routing
if nav_selection == "Home":
    home()
elif nav_selection == "About":
    about()
elif nav_selection == "Disease Detection":
    disease_detection()
elif nav_selection == "Contact":
    contact()
elif nav_selection == "Blogs":
    blogs()







