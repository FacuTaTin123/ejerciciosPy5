'''
7- Calculadora de descuento de compra:
Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
Calcula el precio final después del descuento.
Muestra el precio final al usuario.
'''

precio = float(input("Precio: "))
descuento = float(input("Descuento: "))

print(precio-(precio*(descuento/100)))



