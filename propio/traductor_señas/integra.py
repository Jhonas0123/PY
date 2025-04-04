# Cargar modelo entrenado
model = tf.keras.models.load_model('modelo_señas.h5')

# Predecir en tiempo real
if result.multi_hand_landmarks:
    landmarks = []
    for lm in result.multi_hand_landmarks[0].landmark:
        landmarks.extend([lm.x, lm.y, lm.z])

    prediction = model.predict([landmarks])
    seña_detectada = chr(prediction.argmax() + 65)  # Convertir a letra
    print("Seña detectada:", seña_detectada)
