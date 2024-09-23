# range nos ayuda a establecer un rango de numero que nosotros queramos 
# range siempre inica desde el numero 0 por que que se recorre un numero al lado izquierdo
# ejemplo rango del  1 al 3    (range(4)) 
#   0 <- 1    1 <- 2    2 <- 3     3 <-4
 
# Crear un rango de numeros del 1 al 3
print("numero del 0 al 3")
for n1 in range(4):
    print(n1)

# Crear un rango que inicie desde el 3 al 8
print("numeros del 3 al 7")
for n2 in range(3,8):
    print(n2)

# Crear un rango que inicie del 0 y devuelva numeros de 2 en 2 
print("numeros del 1 al 9 contando de 2 en 2")
for n3 in range(1, 10, 2):
    print(n3)
