'''4- Validador de contraseña:
Solicita al usuario que cree una contraseña.
Verifica si la contraseña cumple con los siguientes criterios:
Tiene al menos 8 caracteres de longitud.
Contiene al menos una letra mayúscula y una letra minúscula.
Tiene al menos un número.
Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
Informa al usuario si la contraseña es válida o no.
'''

print('La contraseña debe tener:\n8 caracteres\nUna mayuscula y una minuscula\nUn numero\nun caracter especial\n')
contraseña = input("Crea una contraseña: ")

if len(contraseña) >= 8:
    list(contraseña)
    for i in contraseña:
            if i.isupper() == True and contraseña.isalnum() == False:    
                    print('buena contraseña')
                    break
                
else:
    print('La contraseña no cumple con los requisitos')

