# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime
import numpy as np
from math import dist, atan2, pi
import warnings
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import onnxruntime as ort
from clases import signos
from ui_carga_inicio import Ui_MainWindow_carga # GUI inicio
from ui_ventana_principal import Ui_MainWindow # GUI principal
from deteccion_manos_pose import DeteccionManosPose

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Path al modelo ONNX
path_modelo_onnx = './modelo/model_transformer_enco_v4.onnx'
# Carga del modelo ONNX
ort_session = ort.InferenceSession(path_modelo_onnx)

class VentanaInicial(QtWidgets.QMainWindow, Ui_MainWindow_carga):

    def __init__(self):
        super(VentanaInicial, self).__init__()
        self.setupUi(self)
        # remueve el titulo del encabezado
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # se vuelve transparente las partes sobre salientes de la ventana
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
  
        # Se aplica el efecto de sombra con color negro
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(9, 36, 43, 150))  # Negro con opacidad 150
        # Se aplica el efecto sombra al widget central
        self.centralwidget.setGraphicsEffect(self.shadow)

        # temporizador de 3 segundos , despues se abre la ventana principal
        QtCore.QTimer.singleShot(3000, self.mostrarVentanaPrincipal)

    def mostrarVentanaPrincipal(self):
        # Se abre la ventana principal
        self.app = VentanaPrincipal()
        self.app.show()
        # Cierra la ventana actual de presentacion
        self.close()
        

class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setupUi(self)

        # Se remueve el encabezado de la ventana
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Se vuelve transparente las partes sobre salientes de la ventana
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.inicio_Button.clicked.connect(self.start_video) # inicio
        self.detener_Button.clicked.connect(self.cancel) # detener
        self.salir_Button.clicked.connect(self.salir) # salir
        self.guardar_Button.clicked.connect(self.guardar_texto)
        self.borrar_Button.clicked.connect(self.borrar_texto) # Borrar todo el texto
        self.borrarultima_Button.clicked.connect(self.borrar_ultima_letra)
        self.umbral_slider.valueChanged.connect(self.actualizarLabelUmbral)
        self.oracion = []

        # Funcion para mover la ventana
        def moveWindow(e):
            # Detecta si la ventana esta de tamano normal
            #if self.isMaximized() == False: # no esta maximizado
                # click izquierdo del mouse presionado
                if e.buttons() == QtCore.Qt.LeftButton:
                    # mueve la ventana
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # Se agrega un detector de eventos de mouse sobre el encabezado
        # para mover la ventana
        self.encabezado_frame.mouseMoveEvent = moveWindow
        # iniciar la interfaz en la parte central
        x, y = self.center()
        self.move(x, y)

    def start_video(self):
        selected_option = self.cam_comboBox.currentText()
        umbral = self.umbral_slider.value()
        self.Work = Work()
        self.Work.camera_num = 1 if selected_option == "Cámara 1" else 0
        self.Work.umbral_detec = round(umbral/100, 2)
        self.Work.start()
        self.Work.imageupd.connect(self.imageupd_slot)
        self.Work.update_texto.connect(self.update_texto_traducido)
        self.Work.update_proba.connect(self.update_texto_proba)

    def imageupd_slot(self, image):
        self.image_label.setPixmap(QtGui.QPixmap.fromImage(image))

    def update_texto_traducido(self, text):
        self.oracion.append(text)
        self.texto_trad_label.setText(f"{''.join(self.oracion)}")

    def update_texto_proba(self, text):
        self.proba_label.setText(text)

    def borrar_ultima_letra(self):
        self.oracion = self.oracion[:-1]
        self.texto_trad_label.setText(f"{''.join(self.oracion)}")

    def borrar_texto(self):
        self.texto_trad_label.clear()
        self.oracion = []

    def cancel(self):
        self.image_label.clear()
        self.Work.stop()

    def guardar_texto(self):
        texto_inferencia = self.texto_trad_label.text()
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        with open("traducciones/traduccion.txt", "a") as txtfile:
                 txtfile.write(f"{date}, {texto_inferencia}\n")

    def actualizarLabelUmbral(self, valor):
        self.umbral_label.setText(f'{valor/100:.2f}')

    def mousePressEvent(self, event):
        # obtención de la posicion del mouse
        self.clickPosition = event.globalPos()

    def center(self):
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height() - 50) // 2
        return x, y

    def salir(self):
        sys.exit()


class Work(QtCore.QThread):
    imageupd = QtCore.pyqtSignal(QtGui.QImage)
    update_texto = QtCore.pyqtSignal(str)
    update_proba = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.camera_num = 0
        self.umbral_detec = 0.50

    def run(self):
        secuencia = []
        #self.oracion = []
        self.hilo_corriendo = True
        self.deteccion = DeteccionManosPose()
        cap = cv2.VideoCapture(self.camera_num, cv2.CAP_DSHOW)
        while self.hilo_corriendo:
            for frame_count in range(30):
                ret, frame = cap.read()
                if not ret:
                    print("Error al capturar el frame")
                    continue
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #flip = cv2.flip(image, 1)
                self.deteccion.mediapipe_detection(frame_rgb)
                # prediccion de puntos
                keypoints = self.deteccion.extraer_keypoints()
                secuencia.append(keypoints)
                frame = self.deteccion.dibujarPosMano(frame)
                # Crear una barra verde delgada en la parte inferior
                barra = np.zeros((5, frame.shape[1], 3), dtype=np.uint8)
                barra[:, :int((frame_count % 30 + 1) / 30 * frame.shape[1]), :] = [0, 255, 0]
                # Superponer la barra en la parte inferior del frame
                frame[-5:, :, :] = barra
                # frame a pyqt
                convertir_qt = QtGui.QImage(frame.data,
                    frame.shape[1],
                    frame.shape[0],
                    QtGui.QImage.Format_BGR888)
                pic = convertir_qt.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
                self.imageupd.emit(pic)

            secuencia = secuencia[-30:]
            if len(secuencia) == 30:
                # datos de entrada prueba
                #print(np.expand_dims(secuencia, axis=0).dtype)
                ort_inputs = {'input': np.expand_dims(secuencia, axis=0).astype(np.float32)}
                # Inferencia del Modelo
                ort_outputs = ort_session.run(None, ort_inputs)[0]
                exp_vector = np.exp(ort_outputs)
                probabilidades = exp_vector / np.sum(exp_vector, axis=1, keepdims=True)

                if probabilidades[0, np.argmax(ort_outputs)] > self.umbral_detec: 
                    #print(signos[np.argmax(ort_outputs)])
                    #self.oracion.append(signos[np.argmax(ort_outputs)])
                    #self.update_texto.emit(f"{''.join(self.oracion)}")
                    self.update_texto.emit(signos[np.argmax(ort_outputs)])
                    #print(probabilidades[0, np.argmax(ort_outputs)])
                    self.update_proba.emit(f"Probabilidad ultima: {probabilidades[0, np.argmax(ort_outputs)]:.3f}")

            time.sleep(2)
        cap.release()

    #def borrar_oracion(self):
    #    self.oracion = []

    def stop(self):
        self.hilo_corriendo = False
        self.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inicio = VentanaInicial()
    inicio.show()
    sys.exit(app.exec())
