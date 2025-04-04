# Si tienes un modelo de machine learning, lo cargas y gestionas aquí.

import tensorflow as tf

# Cargar modelo entrenado
modelo = tf.keras.models.load_model("modelo_señas.h5")

def predecir_sena(landmarks):
    prediction = modelo.predict([landmarks])
    return chr(prediction.argmax() + 65)  # Convierte índice en letra
