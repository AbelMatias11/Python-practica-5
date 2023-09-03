import pandas as pd

# Cargar el DataFrame desde el archivo CSV
df_airbnb = pd.read_csv("Examen 5/airbnb.csv")

# Filtrar las propiedades de Roberto y Clara por sus IDs
roberto_id = 97503
clara_id = 90387

propiedades_roberto_clara = df_airbnb[df_airbnb['room_id'].isin([roberto_id, clara_id])]

# Guardar el DataFrame en un archivo Excel llamado "roberto.xls"
propiedades_roberto_clara.to_excel("Examen 5/roberto.xls", index=False, engine='openpyxl')

# Mostrar el DataFrame resultante
print(propiedades_roberto_clara)