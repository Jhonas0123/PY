import pandas as pd

# Guardar datos en un archivo CSV
data = pd.DataFrame(landmark_list, columns=['x', 'y', 'z'])
data['label'] = 'A'  # Etiqueta de la seña (puedes cambiarla)

data.to_csv('señas_dataset.csv', index=False)
