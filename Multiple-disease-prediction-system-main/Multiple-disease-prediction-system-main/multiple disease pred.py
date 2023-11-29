import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import chatbot 
from chatbot import health_chatbot
from login import login, logout


# loading the saved models

diabetes_model = pickle.load(open('C:\\Users\\HP\\Downloads\\Multiple-disease-prediction-system-main\\Multiple-disease-prediction-system-main\\saved models\\diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('C:\\Users\\HP\\Downloads\\Multiple-disease-prediction-system-main\\Multiple-disease-prediction-system-main\\saved models\\heart_disease_model1.sav','rb'))
parkinsons_model = pickle.load(open('C:\\Users\\HP\\Downloads\\Multiple-disease-prediction-system-main\\Multiple-disease-prediction-system-main\\saved models\\parkinsons_model.sav', 'rb'))

#login 
login_res=login()
if login_res :
    # sidebar for navigation
    with st.sidebar:
        
        selected = option_menu('Multiple Disease Prediction System',
                            
                            
                            ['Home','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                            icons=['house','activity','heart','person'],
                            default_index=0 )
        
        if st.button('Logout'):
            logout()
        
    # Home Page 
    if selected == 'Home':
        
        background_image_style = """
        <style>
        .stApp {
            background-image: url('https://i.imgur.com/WfWutrN.jpg');
            background-size: cover;
        }
        
        </style>
        """
        st.markdown(background_image_style, unsafe_allow_html=True)
        st.markdown('<h1 style="font-size:vw; font-family:Times New Roman ; text-align: center; "> Welccome to MEDSCAN </h1>',unsafe_allow_html=True)
        st.text("")  # Spacer
        st.markdown('<h3 style="color: black; text-align: center;width: 700px; background: rgba(255, 255, 255, 0.5);backdrop-filter: blur(10px);padding: 20px;border-radius: 10px;margin: 20px;"> A Multiple Disease Prediction System</h3>', unsafe_allow_html=True)
        st.text("")  # Spacer
        st.markdown('<h5 style="color: black; text-align: center; width: 700px; text-align: justify; background: rgba(255, 255, 255, 0.5);backdrop-filter: blur(10px);padding: 50px;border-radius: 10px;margin: 20px;">Welcome to our Multiple Disease Prediction System. Explore our predictive tools for diabetes, heart disease, and Parkinsons disease. Simply input your health parameters, and well provide you with risk assessments and valuable insights. Take proactive steps towards a healthier future with our user-friendly, data-driven solutions.</h5>', unsafe_allow_html=True)
    

    # Diabetes Prediction Page
    elif selected == 'Diabetes Prediction':
        
        # page title
        st.markdown('<h1 style="color: black; text-align: center;">Diabetes Prediction using ML</h1>', unsafe_allow_html=True)
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
            
        with col2:
            Glucose = st.text_input('Glucose Level')
        
        with col3:
            BloodPressure = st.text_input('Blood Pressure value')
        
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
        
        with col2:
            Insulin = st.text_input('Insulin Level')
        
        with col3:
            BMI = st.text_input('BMI value')
        
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
        with col2:
            Age = st.text_input('Age of the Person')
        
        
        # code for Prediction
        diab_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
              diab_diagnosis = '<span style="font-weight: bold; font-style: italic; color: red;">The person is diabetic</span>'
            else:
               diab_diagnosis = '<span style="font-weight: bold; font-style: italic; color: green;">The person is not diabetic</span>'
            
        st.markdown(diab_diagnosis, unsafe_allow_html=True)


    # Heart Disease Prediction Page
    elif selected == 'Heart Disease Prediction':
        
        # page title
        st.title('Heart Disease Prediction using ML')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Age = st.text_input('Age')
            Age=int(Age) if Age.isdigit() else 0
            
        with col2:
            # Map user input to numeric values
            sex_mapping = {"F": 0, "M": 1}
            sex_input = st.text_input('Sex (Enter F or M)')
            if sex_input in sex_mapping:
                Sex = sex_mapping[sex_input]
            else:
                st.error('Please enter "F" or "M".')
            
            
        with col3:
            # Map user input to numeric values
            cpt_mapping = {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}
            cpt_input = st.text_input('ChestPaintType (Enter ATA or NAP or ASY or TA)')
            if cpt_input in cpt_mapping:
                ChestPainType = cpt_mapping[cpt_input]
            else:
                st.error('Please enter "ATA" or "NAP" or "ASY" or "TA".')
            
            
        with col1:
            RestingBP = st.text_input('Resting Blood Pressure')
            RestingBP=int(RestingBP) if RestingBP.isdigit() else 0
            
        with col2:
            Cholesterol = st.text_input('Serum Cholestoral in mg/dl')
            Cholesterol=int(Cholesterol) if Cholesterol.isdigit() else 0
            
        with col3:
            FastingBS = st.text_input('Fasting Blood Sugar > 120 mg/dl')
            FastingBS= int(FastingBS) if FastingBS.isdigit() else 0
            
        with col1:
            recg_mapping = {"Normal": 0, "ST": 1, "LVH": 2}
            recg_input = st.text_input('RestingECG (Enter Normal or ST or LVH)')
            if recg_input in recg_mapping:
                RestingECG= recg_mapping[recg_input]
            else:
                st.error('Please enter "Normal" or "ST" or "LVH".')
            
        with col2:
            MaxHR = st.text_input('Maximum Heart Rate achieved')
            MaxHR = int(MaxHR) if MaxHR.isdigit() else 0    
            
        with col3:
            ea_mapping = {"N": 0, "Y": 1}
            ea_input = st.text_input('ExerciseAngina (Enter N or Y)')
            if ea_input in ea_mapping:
                ExerciseAngina = ea_mapping[ea_input]
            else:
                st.error('Please enter "N" or "Y".')
            
        with col1:
            Oldpeak = st.text_input('ST depression induced by exercise')
            Oldpeak = int(Oldpeak ) if Oldpeak.isdigit() else 0
            
        with col2:
            sts_mapping = {"Up": 0, "Flat": 1, "Down": 2}
            sts_input = st.text_input('ST_Slope (Enter Up or Flat or Down)')
            if sts_input in sts_mapping:
                ST_Slope= sts_mapping[sts_input]
            else:
                st.error('Please enter "Up" or "Flat" or "Down".')
            
        # code for Prediction
        heart_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])                          
            
            if (heart_prediction[0] == 1):
               heart_diagnosis = '<span style="font-weight: bold; font-style: italic; color: red;">The person is having heart disease</span>'
            else:
               heart_diagnosis = '<span style="font-weight: bold; font-style: italic; color: green;">The person does not have any heart disease</span>'
            
        st.markdown(heart_diagnosis,unsafe_allow_html=True)
        

    # Parkinson's Prediction Page
    elif selected == "Parkinsons Prediction":
        
        # page title
        st.title("Parkinson's Disease Prediction using ML")
        
        col1, col2, col3, col4, col5 = st.columns(5)  
        
        with col1:
            fo = st.text_input('MDVP Fo(Hz)')
            
        with col2:
            fhi = st.text_input('MDVP Fhi(Hz)')
            
        with col3:
            flo = st.text_input('MDVP Flo(Hz)')
            
        with col4:
            Jitter_percent = st.text_input('MDVP Jitter(%)')
            
        with col5:
            Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
            
        with col1:
            RAP = st.text_input('MDVP RAP')
            
        with col2:
            PPQ = st.text_input('MDVP PPQ')
            
        with col3:
            DDP = st.text_input('Jitter DDP')
            
        with col4:
            Shimmer = st.text_input('MDVP Shimmer')
            
        with col5:
            Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
            
        with col1:
            APQ3 = st.text_input('Shimmer APQ3')
            
        with col2:
            APQ5 = st.text_input('Shimmer APQ5')
            
        with col3:
            APQ = st.text_input('MDVP APQ')
            
        with col4:
            DDA = st.text_input('Shimmer DDA')
            
        with col5:
            NHR = st.text_input('NHR')
            
        with col1:
            HNR = st.text_input('HNR')
            
        with col2:
            RPDE = st.text_input('RPDE')
            
        with col3:
            DFA = st.text_input('DFA')
            
        with col4:
            spread1 = st.text_input('spread1')
            
        with col5:
            spread2 = st.text_input('spread2')
            
        with col1:
            D2 = st.text_input('D2')
            
        with col2:
            PPE = st.text_input('PPE')
            
        
        
        # code for Prediction
        parkinsons_diagnosis = ''
        
        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
               parkinsons_diagnosis = '<span style="font-weight: bold; font-style: italic; color: red;"> The person has Parkinsons disease </span>'
            else:
               parkinsons_diagnosis = '<span style="font-weight: bold; font-style: italic; color: green;"> The person does not have Parkinsons disease </span>'
            
        st.markdown(parkinsons_diagnosis, unsafe_allow_html=True)

    #Chatbot 
    st.sidebar.text("")  # Spacer
    st.sidebar.text("")  # Spacer
    st.sidebar.text("")  # Spacer

    chatbot_response_css = f"""
    <style>
    .chatbot-response-box {{
        width: 200 px ;
        height: 200 px;
        background-color: #BFBFBF;
        border: 1px solid #d4d4d4;
        border-radius: 10px;
        padding: 10px;
        overflow-y: auto;  /* Add scroll bar if the content overflows */
    }}
    </style>
    """
    st.markdown(chatbot_response_css, unsafe_allow_html=True)
    st.sidebar.markdown('<h3 style="color: black;">How may I help you ? </h3>', unsafe_allow_html=True)
    user_question = st.sidebar.text_input("Ask me anything:")
    if user_question:
        bot_response = health_chatbot(user_question)
        st.sidebar.markdown(f'<div class="chatbot-response-box">{bot_response}</div>', unsafe_allow_html=True)
