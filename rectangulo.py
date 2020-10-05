#!/usr/bin/python3

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2

    def calcular_area(self):
        return self.base * self.altura
