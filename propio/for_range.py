# realiza la mitad de un rectangulo en cadena de numeros
numero = int(input("Ingresa numero de con el que se realizara: "))
print("Ejercicio de realizar mitad con un triangulo a la mitad")
for i in range(numero):
    for j in range(i):
        print(i, end=" ")
    print(" ")
    
# realiza la inversa  a la mita de un rectangulo en cadenas de numeros
print("Ejercicio de realizar un triangulo invertido")
b = 0
for i in range(numero, 0, -1):
    b+=1
    for j in range (1, i + 1):
        print(b, end= " ")
    print("\r")

# realizar un triangulo invertido con asteriscos
print("Ejercicio de realizar un triangulo invertido")
k = 2 * numero - 2
for i in range(numero, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
