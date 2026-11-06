# importar librerias 

import pandas as pd
import numpy as np
print("Analisis de datos pacientes Emily Barraza NC = 0025")

pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 110, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]}

df = pd.DataFrame(pacientes)
print(df)

print("+-+-+-+-+- Agrupar por una sola columna Presion_Arterial -+-+-+-+-+-+-")
agrupado = df.groupby('Presion_Arterial')
print(agrupado)
print("+-+-+-+-+- por agregacion -+-+-+-+-+-+-")
# pacientes por fumador
print(agrupado['Fumador'].mean())
print("+-+-+-+-+- por nivel de riesgo maximo-+-+-+-+-+-+-")
# nivel maximo Nivel_Riesgo
print(agrupado['Nivel_Riesgo'].max())

