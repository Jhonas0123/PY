# crear un programa que pida 3 numeros 
# y determine cual es el mayor

num_1 = int(input("ingresa primer numero: "))
num_2 = int(input("ingresa segundo numero: "))
num_3 = int(input("ingresa tercero numero: "))

if num_1 >= num_2 and num_1 >= num_3:
    print(f"el numero {num_1} es mayor")
elif num_2 >= num_1 and num_2 >= num_3:
    print(f"el numero {num_2} es mayor")
elif num_3 >= num_1 and num_3 >= num_2:
    print(f"el numero {num_3} es mayor")
else:
    print("los numeros son iguales")
