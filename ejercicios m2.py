import math

radio = float(input("Ingrese el radio del círculo: "))

# Calcular el perímetro (circunferencia) y el área
perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2

# Mostrar los resultados
print(f"El perímetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")
