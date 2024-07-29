# Ejemplo de funciones Python

def Funcion (numero_1, numero_2):
    return print(f"la suma de los numeros {numero_1} + {numero_2} es = {numero_1 + numero_2}")

n1 = int(input("Coloca el primer numero: "))
n2 = int(input("Coloca el segundo numero: "))

suma = Funcion(n1,n2)
print(suma)