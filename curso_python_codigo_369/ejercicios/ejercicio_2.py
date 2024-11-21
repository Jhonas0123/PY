# EJERCICIO 1
'''crear un programa que pida 2 numeros
y obtenga como resultado cual de ellos 
es par o si ambos lo son''' 

numero = int(input("ingresa el primer numero: "))
numero_2 = int(input("ingresa el segundo numero: "))

if numero % 2 == 0 and numero_2 % 2 == 0:
    print("ambos son pares")
elif numero % 2 == 0 and numero_2 % 2 != 0:
    print(f"el numero {numero} es par")
elif numero % 2 != 0 and numero_2 % 2 == 0:
    print(f"numero 2 {numero_2} es par")
else:
    print("ninguno de los dos numeros son numeros pares")
