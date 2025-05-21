 # editar informacion de un archivo de texto o un archivo de Csv

# Leer un archivo linea por linea
"""with open("E:\Descargas\caperusita.txt", "r") as file:
    for lineas in file:
        print(lineas.strip()) """

#Leer todas las líneas en una lista
"""with open('E:\Descargas\caperusita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#Añadir texto
"""with open('E:\Descargas\caperusita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
# este eliminara todo el texto y solo nos mostrara lo que colocamos
""" with open('E:\Descargas\caperusita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT") """

#conteo lineas de texto
""" with open('E:\Descargas\caperusita.txt', 'r') as file:
    lineas = file.readlines()
    print(len(lineas)) """