# Maneja la captura de video y la detección de manos.

import cv2
import mediapipe as mp

def capturar_manos(procesar_landmarks, predecir_sena):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            landmarks = procesar_landmarks(result.multi_hand_landmarks[0])
            seña_detectada = predecir_sena(landmarks)
            cv2.putText(frame, f'Seña: {seña_detectada}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Traducción de Señales", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Presiona ESC para salir
            break

    cap.release()
    cv2.destroyAllWindows()
