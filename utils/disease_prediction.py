import numpy as np
import joblib
from utils.treatment_advice import get_treatment
from utils.disease_symptoms import SYMPTOM_COLS
# Load the trained disease prediction model
MODEL_PATH = "ml_models/disease_model.pkl"
model = joblib.load(MODEL_PATH)
def predict_disease(symptoms):
    # Create an input vector based on selected symptoms
    input_vector = np.zeros(len(SYMPTOM_COLS))
    for symptom in symptoms:
        if symptom in SYMPTOM_COLS:
            index = SYMPTOM_COLS.index(symptom)
            input_vector[index] = 1
    # Make prediction
    prediction = model.predict([input_vector])[0]
    # Get treatment advice
    treatment = get_treatment(prediction)
    return prediction, treatment
