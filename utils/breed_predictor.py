import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
MODEL_PATH = os.path.join("ml_models", "breed_classifier", "breed_model.h5")
CLASS_NAMES = {
    0: "Broiler - Noiler",
    1: "Cockerel",
    2: "Layer"
}
model = load_model(MODEL_PATH)
def predict_breed(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    predictions = model.predict(img_array)[0]
    predicted_index = np.argmax(predictions)
    confidence = round(float(predictions[predicted_index]) * 100, 2)
    predicted_class = CLASS_NAMES[predicted_index]
    return predicted_class, confidence
