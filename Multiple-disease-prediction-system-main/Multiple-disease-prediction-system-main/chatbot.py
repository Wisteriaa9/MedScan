def health_chatbot(question):
    question = question.lower()
    if "diabetes" in question:
        return "Diabetes is a chronic condition that affects how your body processes glucose. You can check your diabetes risk using our Diabetes Prediction tool!"
    elif "heart disease" in question:
        return "Heart disease refers to a variety of conditions that affect the heart. Use our Heart Disease Prediction tool to assess your risk!"
    elif "parkinson" in question:
        return "Parkinson's disease is a neurodegenerative disorder. You can check your risk of Parkinson's using our Parkinson's Prediction tool."
    elif "insulin" in question:
        return "Insulin is a hormone that helps regulate your blood sugar levels. It's important in diabetes management."
    elif "bmi" in question:
        return "BMI (Body Mass Index) is a measure of body fat based on your weight and height. It can indicate whether you're underweight, normal weight, overweight, or obese."
    elif "serum" in question:
        return "Serum Cholestoral in mg/dl measures the level of cholesterol in your blood, which can affect heart health."
    elif "angina" in question:
        return "Exercise-induced angina is chest pain or discomfort that occurs when the heart doesn't receive enough oxygen during physical activity."
    elif "resting electrocardiographic results" in question:
        return "Resting electrocardiographic results provide information about the heart's electrical activity and can help diagnose heart conditions."
    elif "st" in question:
        return "ST depression induced by exercise is a measure of abnormal changes in the ECG pattern during exercise, which can indicate heart problems."
    elif "thal" in question:
        return "Thalassemia is a blood disorder. Thal values indicate types of defects in the blood's oxygen-carrying capacity."
    elif "sex" in question:
        return "Sex is a demographic factor. It's used in health predictions and assessments."
    elif "maximum heart rate achieved" in question:
        return "Maximum heart rate achieved is the highest heart rate a person can achieve during exercise and can be used for health assessments."
    elif "slope of the peak exercise ST segment" in question:
        return "The slope of the peak exercise ST segment indicates the pattern of ST-segment changes during exercise."
    elif "chest pain" in question:
        return "Chest pain types can indicate various heart and health conditions. They are categorized based on symptoms."
    elif "fasting blood sugar > 120 mg/dl" in question:
        return "Fasting blood sugar > 120 mg/dl suggests high blood sugar levels, which can be a risk factor for diabetes and heart disease."
    elif "flourosopy" in question:
        return "The number of major vessels colored by fluoroscopy indicates blood flow in the heart's major arteries."
    elif "mdvp fo" in question:
        return "MDVP Fo(Hz) is a measure of fundamental frequency in voice analysis and is used in diagnosing voice disorders."
    elif "mdvp rap" in question:
        return "MDVP RAP is related to voice jitter and can help diagnose voice disorders."
    elif "shimmer apq3" in question:
        return "Shimmer APQ3 measures variations in voice amplitude and pertains to voice quality assessment."
    elif "hnr" in question:
        return "HNR (Harmonics-to-Noise Ratio) measures the ratio of harmonics to noise in voice signals and is used in voice analysis."
    elif "d2" in question:
        return "D2 is a measure related to chaos in voice signals and is used in voice disorder diagnosis."
    elif "fhi(hz)" in question:
        return "MDVP Fhi(Hz) is a high-frequency component in voice analysis and is used for voice disorder assessment."
    elif "ppq" in question:
        return "MDVP PPQ is a perturbation quotient related to voice jitter and is used for voice disorder diagnosis."
    elif "apq5" in question:
        return "Shimmer APQ5 is similar to APQ3 and measures voice quality variations."
    elif "rpde" in question:
        return "RPDE (Recurrence Period Density Entropy) measures voice signal complexity in voice analysis."
    elif "ppe" in question:
        return "PPE (Pitch Period Entropy) is used in voice analysis to assess pitch and voice quality."
    else:
        return "I'm a health chatbot. Feel free to ask me any health-related questions!"