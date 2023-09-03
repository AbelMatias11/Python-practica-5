import pandas as pd

serie_numeros = pd.Series([10, 20, 10])

serie_colores = pd.Series(['rojo', 'verde', 'azul'])

df = pd.DataFrame()

df['numeros'] = serie_numeros

df['colores'] = serie_colores

avengers = pd.read_csv('Examen 5/avengers.csv')

print(avengers.head())

print(avengers.head(10))

print(avengers.tail())

print(avengers.shape)

print(avengers.dtypes)

avengers.set_index('fecha_inicio', inplace=True)

avengers.sort_index(ascending=False, inplace=True)

avengers.reset_index(inplace=True)