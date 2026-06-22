import random
import string

print(" GENERADOR SEGURO DE CONTRASEÑAS ")


while True:
    longitud = input("Ingrese la longitud de la contraseña: ")

    if longitud.isdigit():
        longitud = int(longitud)
        break
    else:
        print("Solo debe ingresar números.")

usar_mayusculas = input("¿Desea usar MAYÚSCULAS? (s/n): ")
usar_minusculas = input("¿Desea usar minúsculas? (s/n): ")
usar_numeros = input("¿Desea usar números? (s/n): ")
usar_simbolos = input("¿Desea usar símbolos? (s/n): ")

caracteres = ""

if usar_mayusculas.lower() == "s":
    caracteres += string.ascii_uppercase

if usar_minusculas.lower() == "s":
    caracteres += string.ascii_lowercase

if usar_numeros.lower() == "s":
    caracteres += string.digits

if usar_simbolos.lower() == "s":
    caracteres += string.punctuation

if caracteres == "":
    print("ERROR: Debe seleccionar al menos un tipo de carácter.")
else:
    
    contraseña = ""

    for i in range(longitud):
        contraseña += random.choice(caracteres)

    print("Contraseña generada:")
    print(contraseña)
    