#!/usr/bin/python3
from rectangulo import Rectangulo
import math

class TrianguloRecto(Rectangulo):
    
    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base*self.base + self.altura*self.altura)
        return hipotenusa + self.base + self.altura

    def calcular_area(self):
        return super().calcular_area() / 2

