# Contiene funciones para extraer landmarks y predecir señas.

import numpy as np

def procesar_landmarks(hand_landmarks):
    landmarks = []
    for lm in hand_landmarks.landmark:
        landmarks.extend([lm.x, lm.y, lm.z])
    return np.array(landmarks)

def predecir_sena(landmarks):
    # Simulación de predicción; reemplaza esto con tu modelo entrenado
    return "A"  # Ejemplo: siempre devuelve "A"
