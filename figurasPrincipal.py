import pandas as pd

from funciones import triangulo, rectangulo, circulo

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []


for index, row in dataFile.iterrows():
	print(f"Fila {index}: FIGURA = {row['FIGURA']}, MEDIDA1 = {row['MEDIDA1']}, MEDIDA2 = {row['MEDIDA2']}") 
	if row['FIGURA']  == "t":
		area = triangulo(row['MEDIDA1'], row['MEDIDA2'])
		areas.append(area)
		
	elif row['FIGURA']  == "r":
                area = rectangulo(row['MEDIDA1'], row['MEDIDA2'])
                areas.append(area)

	elif row['FIGURA']  == "c":
                area = circulo(row['MEDIDA1'])
                areas.append(area)

print(f"Las areas de las figuras son: {areas}")
