# utils/disease_predictor.py
from utils.disease_prediction import predict_disease
from utils.disease_symptoms import SYMPTOM_COLS
def get_prediction(symptoms_selected):
    prediction, treatment = predict_disease(symptoms_selected)
    return prediction, treatment
def get_all_symptoms():
    return SYMPTOM_COLS