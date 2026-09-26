"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

# Implementar el paradigma estructurado

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

area = base * altura

print("El área del rectángulo es:", area)


# Implementar el paradigma Orientado a Objetos (OO)

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = float(input("\nIngresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

rectangulo = Rectangulo(base, altura)

print("El área del rectángulo es:", rectangulo.calcular_area())