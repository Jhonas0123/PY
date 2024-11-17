import cv2
# Inicializar la cámara
# aqui hay que probar con distintos numeros para ver
#cual numero es el de nuestra camara en nuestro caso 
# la posicion es la camara 0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error al abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mostrar la imagen
    cv2.imshow('Deteccion', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
