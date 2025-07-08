import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.udemy.com/"

# realizar la peticion requests

response = requests.get(url)

# aqui nos dara la respuesta que es 200 nuestra solicitur fue exitosa 

# print(response)

# para ver la respuesta pero de forma html

# print(response.text)

# con if verificamos que sea una solicitud correcta y que nos de
# los primeros 10 caracteres

if response.status_code == 200:
    print("Status code: 200.exitoso")
    print(response.text[0:50])
else: # si el url esta erroneo nos muesra el error que corresponde
    print("Status code:", response.status_code) 