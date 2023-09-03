import pandas as pd

df_airbnb = pd.read_csv("Examen 5/airbnb.csv")

alicias_requisitos = df_airbnb[(df_airbnb['reviews'] > 10) & (df_airbnb['overall_satisfaction'] > 4)]

alicias_requisitos.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False], inplace=True)

mejores_alojamientos = alicias_requisitos.head(3)

print(mejores_alojamientos[['room_id', 'neighborhood', 'overall_satisfaction', 'reviews']])
