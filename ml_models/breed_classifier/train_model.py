import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
# Paths
BASE_DIR = "ml_models/breed_classifier"
DATA_DIR = os.path.join(BASE_DIR)
MODEL_PATH = os.path.join(BASE_DIR, "breed_model.h5")
# Parameters
IMG_SIZE = (150, 150)
BATCH_SIZE = 16
EPOCHS = 10
# 1. Prepare Image Data
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)
train_generator = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)
val_generator = datagen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)
# 2. Build CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    MaxPooling2D(2,2),
    
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')  # 3 classes: broiler, cockerel, layer
])
# 3. Compile Model
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# 4. Train Model
model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=val_generator
)
# 5. Save Model
model.save(MODEL_PATH)
print(f"✅ Model saved to {MODEL_PATH}")
