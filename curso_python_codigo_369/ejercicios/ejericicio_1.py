# importamos la libreria de math para trabajar con pi=n
import math
# pasar la ecuacuib a una expresion algoritmica

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r=((c+5)*(b**2-3*a*c)*a**2)/(4*a)

# intercambiar valores de A a B y de B a A

a = input("a: ")
b = input("b: ")

a,b = b,a
print(f"el numero de a es {a}")
print(f"el numero de a es {b}")

#obtener el radio y longitud de un circulo en python

radio = float(input("ingresa el radio: "))
area = math.pi*r**2
longitud = 2*math.pi*r
print(f"el area es: {area}, la longitud es: {longitud}")

# obtener el precio final que se tiene que pagar si se aplica el 36 % de descuento
# del total de la compra
precio = float(input("ingrese el precio: "))
descuento = precio * (36*1/100)
precio_final = precio - descuento
print(f"el precio final es {precio_final}")