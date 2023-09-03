import pandas as pd
import matplotlib.pyplot as plt

df_airbnb = pd.read_csv("Examen 5/airbnb.csv")

presupuesto_diana = 50
propiedades_diana = df_airbnb[(df_airbnb['room_type'] == 'Shared room') & (df_airbnb['price'] <= presupuesto_diana)]

propiedades_diana = propiedades_diana.sort_values(by='overall_satisfaction', ascending=False)

top_10_propiedades = propiedades_diana.head(10)

room_type_counts = df_airbnb['room_type'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(room_type_counts, labels=room_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Tipo de Habitaciones')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

print(top_10_propiedades[['room_id', 'neighborhood', 'overall_satisfaction', 'price']])