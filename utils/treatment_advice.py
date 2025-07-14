# utils/treatment_advice.py
TREATMENT_GUIDE = {
    "Infectious Bronchitis": "Provide vitamins and isolate infected birds",
    "Coccidiosis": "Use anticoccidial drugs like Amprolium",
    "Egg Drop Syndrome": "Improve nutrition and calcium. Remove infected birds",
    "Fowl Typhoid": "Use Furazolidone. Improve sanitation",
    "Avian Influenza": "Report to vet authority. No specific treatment",
    "Newcastle Disease": "Use vaccines and maintain biosecurity",
    "Arthritis": "Use anti-inflammatory drugs",
    "Fowl Cholera": "Use Sulfa drugs and isolate infected birds",
    "Infectious Coryza": "Use Tylosin or Erythromycin",
    "Eimeria": "Give anticoccidials and clean litter",
    "Pullorum": "Use Furazolidone and isolate chicks",
    "Bird Flu": "No treatment. Quarantine and notify authorities",
    "Chronic Respiratory Disease": "Use Tylosin and improve ventilation",
    "Sour Crop": "Empty crop and provide soft feed",
    "Multiple Risk": "Improve housing, nutrition and hygiene",
    "Fowl Pox": "No specific treatment. Vaccinate healthy birds",
    "Unknown": "Consult a veterinarian for detailed examination"
}
def get_treatment(disease):
    return TREATMENT_GUIDE.get(disease, "Consult a veterinarian for diagnosis and treatment.")
