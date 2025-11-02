import math

def triangulo(MEDIDA1, MEDIDA2):
	area = (MEDIDA1 * MEDIDA2) / 2
	perimetros = MEDIDA1 * 3 
	return area, perimetros

def rectangulo(MEDIDA1, MEDIDA2):
        area = (MEDIDA1 * MEDIDA2)
        perimetros = 2 * (MEDIDA1 + MEDIDA2)
        return area, perimetros

def circulo(MEDIDA1):
        area = math.pi * (MEDIDA1 ** 2)
        perimetros = 2 * * math.pi * MEDIDA1
        return area, perimetros
