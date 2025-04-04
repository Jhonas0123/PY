# Este archivo se encarga de iniciar el programa y coordinar las demás partes del proyecto.

from captura import capturar_manos
from procesamiento import procesar_landmarks, predecir_sena

def main():
    capturar_manos(procesar_landmarks, predecir_sena)

if __name__ == "__main__":
    main()
