#!/usr/bin/python3

from trianguloRecto import TrianguloRecto
from rectangulo import Rectangulo
from cuadrado import Cuadrado

print("Ingrese el tipo de figura")
tipo = int(input("1: TriánguloRecto - 2: Rectángulo - 3: Cuadrado "))
if tipo == 3:
    lado = int(input("Ingrese el lado: "))
    figura = Cuadrado(lado)
elif tipo == 2 or tipo == 1:
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    if tipo == 1:
        figura = TrianguloRecto(base, altura)
    else:
        figura = Rectangulo(base, altura)
else:
    print("Error: tipo de figura desconocida")
    exit()

print("La figura pertenece a la clase " + type(figura).__name__)
print("Su base es " + str(figura.base) + " y su altura es " + str(figura.altura))
print("Su area es " + str(figura.calcular_area()))
print("Su perímetro es " + str(figura.calcular_perimetro()))

