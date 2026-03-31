'''3- Generador de secuencia Fibonacci:
Pide al usuario que ingrese un número entero positivo.
Genera los primeros n números de la secuencia Fibonacci, donde n es el número ingresado por el usuario.
Muestra la secuencia Fibonacci resultante.
'''

numero = int(input("pon un numero entero y positivo: "))

list = [0,numero]

for i in range(6):
    list.append(list[i] + list[i+1])
      

print(list)
