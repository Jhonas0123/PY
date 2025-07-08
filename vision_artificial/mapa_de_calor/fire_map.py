# primero llamamos a las librerias que necesitaremos
import cv2
import numpy as np
import matplotlib.pyplot as plt

# llamamos al video (mejor si colocamos la ubicacion exacta)
video_path = "/vision_artificial/mapa_de_calor/store-aisle-detection.mp4"

# abrimos y cargamos nuestro video con cv2
cap = cv2.VideoCapture(video_path)

# usamos un metodo de opencv que nos ayuda detectar entre cada frame
# movimientos de todo lo que se aparesca con movimiento
bg_substractor = cv2.createBackgroundSubtractorMOG2(
    history=500,            # numero de frames usados para construir el fondo
    varThreshold=16,        # sensibilidad para detectar cambios
    detectShadows=True,     # deteccion de sombras
)

# vamos a superponer el mapa de calor con el video actual
heatmap_acumulado = None

while True:                 
    ret, frame = cap.read() # empezamos a leer el video
    if not ret:
        break

    # inciamos el acumulador 
    if heatmap_acumulado is None:
        heatmap_acumulado = np.zeros_like(frame.shape[:2], dtype=np.float32)

    # aplicamos sustraccion de fondo -> las areas en movimiento (objetos) se resaltan
    fgmask = bg_substractor.apply(frame)

    # acumular la mascara ( convertida a float para evitar saturacion)
    heatmap_acumulado = cv2.add(heatmap_acumulado, fgmask.astype(np.float32))

# mostrar el mapa de calor 
plt.imshow(heatmap_acumulado, cmap="hot")
plt.title("heatmap acumulado")
plt.axis("off")
plt.show()