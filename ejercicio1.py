'''Es un indicador utilizado para evaluar si una persona tiene un peso saludable en relación con su altura. 
Se calcula dividiendo el peso en kilogramos por el cuadrado de la altura en metros. 
Según el resultado, se clasifica en diferentes categorías como bajo peso, normal, sobrepeso u obesidad.'''


peso = float(input("Peso: "))
altura = float(input("Altura: "))

if altura > 0:
    imc = peso / (altura ** 2)
    print("IMC:", imc)

    if imc < 18.5:
        print("Bajo peso")
        print('sos s')
    elif 18.5 <= imc < 25:
        print("Peso normal")
        print('sos m')
    elif 25 <= imc < 30:
        print("Sobrepeso")
        print('sos l')
    else:
        print("Obesidad")
        print('sos xl')