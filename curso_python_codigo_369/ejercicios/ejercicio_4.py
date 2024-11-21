'''
crear un programa que compare dos nombres, y 
verificar si hay coincidenciao no, si es que
 ambos nombres comienzan con la misma letra o si 
terminan con la misma letra.
'''

nom_1 = input("nombre 1: ")
nom_2 = input("nombre 2: ")
if nom_1 [0] == nom_2 [0] or nom_1 [-1] == nom_2 [-1]:
    print ("si hay coincidencia")
else:
    print("no se cumple las condiciones")