'''5- Juego de adivinanza de números:
Genera un número aleatorio entre 1 y 100.
Pide al usuario que adivine el número.
Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
Muestra el número de intentos necesarios para adivinar.
'''
import random

aleatorio = random.randint(1, 100)
print('el numero es', aleatorio, ' pero no le digas a nadie\n')

print('El juego trata de que adivines el numero\n')

while True:
    jugador = int(input('pon un numero: '))
    if jugador < aleatorio:
        print('muy chico')
    elif jugador > aleatorio:
        print('muy grande')
    else:
        print('ganaste')
        break