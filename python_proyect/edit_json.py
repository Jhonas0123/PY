import json

#Lectura del archivo
""" with open('productos.json', mode='r') as file:
    products = json.load(file) """

#Mostrar el contenido
""" for product in products:
    #print(product)
    print(f"Product: {product['name']}, Price: {product['price']}") """


# abrimos el archivo json
file_path = 'productos.json'
# creamos el nuevo archivo
new_product = {
    "name": "cargador inalambrico",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}
# primero abrimos en modo lectura
with open(file_path, mode='r') as file:
    products = json.load(file)

# añadimos el nuevo producto a archivo json en modo lectura ya visto
products.append(new_product)

# abrimos sobre el mismo archivo de modo escritura y esto estara almacenado en archivo
# y pasamos los parametros, la informacion. el archivo y la identacion
# esto es un cambio de estado para añadir informacion
with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)