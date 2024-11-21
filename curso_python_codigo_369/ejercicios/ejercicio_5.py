'''
crear un programa que simule un cajero
automatico con un saldo inicial de $ 2000,
con el siguiente menu:

1.- ingreso de dinero
2.- retirar dinero
3.- mostrar dinero
4.- salir
 
'''
saldo = 2000
print(f"""**** MERNU ****
      1.- ingreso de dinero:
      2.- retirar dinero:
      3.- mostrar dinero:
      3.- salit""")

opcion = int(input("ingresa una opcion"))

if opcion == 1:
    ingreso = float(input("ingresa el monto que quieres ingresar: "))
    saldo += ingreso
    print (f"el saldo que ingreso es {ingreso} saldo total : {saldo}")
elif opcion == 2:
    retiro = float(input("ingresa el monto que quieres ingresar: "))
    if retiro < saldo:
        saldo -= retiro
        print (f"el saldo que ingreso es {retiro} saldo total : {saldo}")
    else:
        print("no cuentas con el saldo suficiente para hacer este tipo de retiro")    
elif opcion == 3:
    print (f"el dinero que tienes de saldo es: {saldo}")
elif opcion == 4:
    print ("salir del programa")
else: 
    print("ingresa un numero valido")





