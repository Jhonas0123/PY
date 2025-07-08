
'''
usando las cuatro fundamentales
'''

mi_archivo = open("D:/clases Git y GIT HUB/PY/curso/recetario/prueba.txt")

# imprime el texto dentro del archivo txt
todo = mi_archivo.read()
print(todo)

# imprime solo la primera linea del archivo
una_linea = mi_archivo.readline()
# print(una_linea)

# imprime sin el salto que realiza al imprimir
una_linea = (mi_archivo.rstrip())
# print(una_linea)

# imprime la linea pero en mayusculas
una_linea = (mi_archivo.upper())
# print(una_linea)

# con un for

for l in mi_archivo:
    print("aqui dice: " + l)

# para crear una lista con todos los elementos del archivo o todas las lineas
todas = mi_archivo.readlines()

# siempre que se trabaje con la apertura de una archivo
# lo debemos cerrar para resguardar el espacio de memoria
# del ordenador

mi_archivo.close()