import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear modelo
model = Sequential([
    Dense(128, activation='relu', input_shape=(63,)),  # 21 puntos * 3 coordenadas
    Dense(64, activation='relu'),
    Dense(26, activation='softmax')  # 26 letras del alfabeto
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Cargar datos del dataset
# X: características (puntos clave), y: etiquetas (letras)
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
