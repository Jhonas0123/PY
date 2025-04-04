import cv2
import mediapipe as mp
from math import dist, atan2, pi

class DeteccionManosPose():
    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5):

        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_holistic = mp.solutions.holistic # modelo Holistic
        self.holistic = self.mp_holistic.Holistic(
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence)
        self.mp_drawing = mp.solutions.drawing_utils # Utilidades de dibujo

        self.pose_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

    def mediapipe_detection(self, frame_rgb):
        # frame rgb
        frame_rgb.flags.writeable = False  # Imagen no editable
        self.results = self.holistic.process(frame_rgb)  # predicción de puntos
        #return self.results

    def dibujarPosMano(self, frame):

        def dibujar_contorno_mano(landmarks, frame):
            H, W, _ = frame.shape
            x = [landmark.x for landmark in landmarks.landmark]
            y = [landmark.y for landmark in landmarks.landmark]

            x1 = int(min(x) * W) - 10
            y1 = int(min(y) * H) - 10
            x2 = int(max(x) * W) + 10
            y2 = int(max(y) * H) + 10

            cv2.rectangle(frame, (x1, y1), (x2, y2), (34, 147, 238), 4)

        if self.results.right_hand_landmarks:
            dibujar_contorno_mano(self.results.right_hand_landmarks, frame)

        if self.results.left_hand_landmarks:
            dibujar_contorno_mano(self.results.left_hand_landmarks, frame)

        return frame

    # calculo de distancias y angulos apartir de las coordenadas (x,y)
    def extraer_keypoints(self):
        x_minl = min([landmark.x for landmark in self.results.left_hand_landmarks.landmark]) if self.results.left_hand_landmarks else 0
        y_minl = min([landmark.y for landmark in self.results.left_hand_landmarks.landmark]) if self.results.left_hand_landmarks else 0
        x_minr = min([landmark.x for landmark in self.results.right_hand_landmarks.landmark]) if self.results.right_hand_landmarks else 0
        y_minr = min([landmark.y for landmark in self.results.right_hand_landmarks.landmark]) if self.results.right_hand_landmarks else 0
        
        lh = [coord for landmark in self.results.left_hand_landmarks.landmark for coord in (landmark.x - x_minl, landmark.y - y_minl)] \
                if self.results.left_hand_landmarks else [0]*42 # distancias entre los puntos minimos de la mano izquierda y los demas dedos
        rh = [coord for landmark in self.results.right_hand_landmarks.landmark for coord in (landmark.x - x_minr, landmark.y - y_minr)] \
                if self.results.right_hand_landmarks else [0]*42 # distancias entre los puntos minimos de la mano derecha y los demas dedos
        c_nx = self.results.pose_landmarks.landmark[0].x if self.results.pose_landmarks else 0.5 
        c_ny = self.results.pose_landmarks.landmark[0].y if self.results.pose_landmarks else 0.2 # coordenada de la nariz, punto de referecia origen
        distancias_rh = [dist((landmark.x, landmark.y), (c_nx, c_ny)) for landmark in self.results.right_hand_landmarks.landmark] \
                if self.results.right_hand_landmarks else [0]*21 # distancia de cada dedo al punto de referencia
        distancias_lh = [dist((landmark.x, landmark.y), (c_nx, c_ny)) for landmark in self.results.left_hand_landmarks.landmark] \
                if self.results.left_hand_landmarks else [0]*21 
        angulos = [atan2((self.results.pose_landmarks.landmark[idx].y - c_ny), (self.results.pose_landmarks.landmark[idx].x - c_nx))/(2*pi) for idx in self.pose_list] \
                if self.results.pose_landmarks else [0]*12 # angulos del hombro, antebrazo, brazo y la muñeca con respecto al punto de referencia
        # 138 features en total
        return rh + distancias_rh + angulos + lh + distancias_lh

