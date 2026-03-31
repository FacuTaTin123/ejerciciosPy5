'''
8- Generador de contraseñas aleatorias:
Solicita al usuario que ingrese la longitud deseada para la contraseña.
Genera una contraseña aleatoria con la longitud especificada.
Utiliza caracteres alfanuméricos y caracteres especiales para mayor seguridad.
Muestra la contraseña generada al usuario.
'''
import random

longitud = int(input('Longitud de la contraseña: '))

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

lista = []

largo = len(caracteres)

for i in range(longitud):
    
    p = random.randint(1, largo-1)
    lista.append(caracteres[p])
    contra = "".join(lista)
print(contra)