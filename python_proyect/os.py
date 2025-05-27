import os

# obtener el directorio actual 
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)

# listar los archivos .txt
json_files = [f for f in os.listdir(".") if f.endswith(".json")]
print("archivos txt: ", json_files)

# renonmbrar archivo
os.rename("calculadora_class", "calculadora.py")
print("archivo renombrado")