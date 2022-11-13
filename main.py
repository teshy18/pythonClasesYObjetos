import string


# Ejercicio 5, Python, OpenBootCamp

class Vehiculo():
    Color: string = 'blanco'
    Ruedas: int = 4
    Puertas: int = 2


class Coche(Vehiculo):
    Velocidad: float
    Cilindarda: float


Fiat = Coche()

print('')
print(Fiat)
print('')
print('El color del Fiat es: ' + Fiat.Color)