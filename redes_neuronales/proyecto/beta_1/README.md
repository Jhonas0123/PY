# 🖐️ Traductor del deletreo manual de la Lengua de Señas Boliviana a texto 🇧🇴

Programa traductor de la lengua se señas boliviana a texto  utilizando Pytorch y PyQt5. El programa fue entrenado para reconocer el alfabeto dactilologico boliviano, numeros del 0-10 y otras 19 palabras, con el fin de desarrollar un modelo que sea capaz predecir tanto **señas estáticas como dinámicas**. El tamaño del conjunto de datos fue de 5800 secuencias capturadas con ayuda de Mediapipe. El modelo fue desarrollado utilizando el framework de aprendizaje profundo [Pytorch](https://pytorch.org/) y [Pytorch lightning](https://lightning.ai/). La interfaz de usuario se creo usando la libreria PyQt5, que puede ser actualizado a la version 6.

Se utilizo el bloque `Transformer Encoder` de la arquitectura Transformers publicado en el paper [Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) para realizar la clasificación de secuencias, que en este caso se captura la posicion de las manos y la pose del cuerpo utilizando la camara frontal del computador con OpenCV y Mediapipe. No se entrena al modelo con los puntos o coordenadas obtenidos sino que se realizo un proceso de data Augmentation para obtener mejores relaciones o caracteristicas para la etapa de aprendizaje. Se calculo distancias dentro de las manos y fuera de ellas, asi como tambien angulos. 

El programa puede ser ejecutado con Python o mediante un ejecutable .exe para windows sin necesidad de instalar librerias externas (opción 1). Para su ejecución con Python seguir el proceso de instalación de la opción 2.

## Opción 1: Programa ejecutable para Windows

El programa puede ser descargado del siguiente link (179 MB): https://drive.google.com/drive/folders/1eIwQcELxASIz4WhQICrakfWjcq_kSUj1?usp=sharing , no se necesita instalar nada externo. Solo descomprimir el archivo .rar y encontrara el programa como Traductor_LSB.exe

## Opción 2: Instalación con Python

- Instalar [Python](https://www.python.org/downloads/). La version utilizada en este proyecto fue Python 3.10.10
- Descargar o clonar el codigo en una carpeta con git.

```bash
git clone https://github.com/freddxvill/Proyecto_Traductor_de_la_LSB
```
- Crear un **entorno virtual** de python dentro de la carpeta. Con [virtualenv](https://virtualenv.pypa.io/en/latest/) utilizar el siguiente comando:

```bash
virtualenv venv
```
- **Activa** el entorno. En Windows con Powershell:

```bash
.\venv\Scripts\activate
```
- Instalar las dependencias del archivo **requirements.txt** en el entorno.

```bash
pip install -r requirements.txt
```

## Ejecución del programa

Ejecutar el archivo Traductor_LSB.py (con el entorno activado)

```bash
python Traductor_LSB.py
```

Se mostrara la interfaz de usuario del programa.

[![GUI-LSB.png](https://i.postimg.cc/PfzPJpXT/GUI-LSB.png)](https://postimg.cc/9z0WNfwn)


## Funcionamiento del programa

El programa inicia pulsando el boton iniciar. Se debe seleccionar la camara, 0 indica que se usara la camara interna del computador en otro caso sera una camara externa conectada. El programa captura a una persona realizando una seña durante 30 fotogramas, ya sea una seña estática o dinámica. Luego de los 30 fotogramas capturados, los datos se envian al modelo para realizar la prediccion de la seña. El program muestra debajo la letra,número o palabra predicha. El texto predicho se va concatenando formando asi oraciones mas largas.

## Arquitectura del modelo

[![git-lsb-proyect.png](https://i.postimg.cc/qvD6Ykrh/git-lsb-proyect.png)](https://postimg.cc/nX7L9fCp)

## Señas Reconocidas por el programa

Se reconocen 58 clases o señas, que cubren tanto señas estáticas como dinámicas.

<div align="center">

| Clase | Codificación | Clase        | Codificación |
|:-----:|:------------:|:------------:|:------------:|
| 0     | 0            | R            | 29           |
| 1     | 1            | S            | 30           |
| 2     | 2            | T            | 31           |
| 3     | 3            | U            | 32           |
| 4     | 4            | V            | 33           |
| 5     | 5            | W            | 34           |
| 6     | 6            | X            | 35           |
| 7     | 7            | Y            | 36           |
| 8     | 8            | Z            | 37           |
| 9     | 9            | espacio      | 38           |
| 10    | 10           | Hola         | 39           |
| A     | 11           | Buenos días  | 40           |
| B     | 12           | Gracias      | 41           |
| C     | 13           | Por favor    | 42           |
| D     | 14           | Yo           | 43           |
| E     | 15           | Abogado      | 44           |
| F     | 16           | Doctor       | 45           |
| G     | 17           | Electricista | 46           |
| H     | 18           | Policía      | 47           |
| I     | 19           | Presidente   | 48           |
| J     | 20           | Profesor     | 49           |
| K     | 21           | Nombre       | 50           |
| L     | 22           | ser/estar    | 51           |
| LL    | 23           | Mi           | 52           |
| M     | 24           | Trabajo      | 53           |
| N     | 25           | La Paz       | 54           |
| Ñ     | 26           | Sucre        | 55           |
| O     | 0           | Cochabamba   | 56           |
| P     | 27           | Vivir        | 57           |
| P     | 28           |         |          |

</div>


## Notas

- Se puede implementar un pipeline de reentrenamiento. Esto se sigue desarrollando y lo tendra en una version futura.
- Los datos utilizados se guardaron en formato Zarr, ya que maneja y reduce el tamaño de arreglos multidimensionales que alimentan al modelo. Las etiquetas se guardaron en vectores con formato numpy.
- La captura de la seña se debe realizar a una distancia de 60 +- 10cm con respecto a la camara frontal.
- EL nivel de luz se debe encontrar dentro del rango de 70 y 150 Lux para el uso de la herramienta de traducción.
