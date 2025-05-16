""" desarrollar una calculadora en python con funciones """

def suma(a1, a2):
    return a1+a2

def resta(a1, a2):
    return a1-a2

def multiplicacion(a1, a2):
    return a1*a2

def division(a1, a2):
    return a1/a2

def calculadora():
    print("""**Calculadora**
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir""")
    
    opcion = int(input("ingresa un numero del 1 al 5 para acceder a una funcion: "))

    if opcion == 5:
        print("gracias por usar la calculadora")
        return
        

    if opcion in [1,2,3,4]:
        d1 = float(input("ingresa el primer valor: "))
        d2 = float(input("ingresa el segundo valor: "))
        if opcion == 1: 
            print(f"la suma es {suma(d1, d2)}")
        elif opcion == 2: 
            print(f"la resta es {resta(d1, d2)}")
        elif opcion == 3: 
            print(f"la multiplicacion es {multiplicacion(d1, d2)}")
        elif opcion == 4: 
            print(f"la divicion es {division(d1, d2)}")
    else:
        print("la opcion es incorrecta")
    
calculadora()
