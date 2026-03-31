'''La conversión entre grados Celsius y Fahrenheit se basa en una escala de temperatura 
donde 0 °C es el punto de congelación del agua y 100 °C es el punto de ebullición. 
En la escala Fahrenheit, estos valores corresponden aproximadamente a 32 °F y 212 °F, respectivamente.'''

celcios = float(input("Grados en C: "))
farenheid = (celcios * 9/5) + 32
print("Grados en F:", farenheid)
