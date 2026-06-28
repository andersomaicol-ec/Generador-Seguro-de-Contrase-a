import secrets
import string

print("   GENERADOR SEGURO DE CONTRASEÑAS")

while True:

    while True:
        longitud = input("\nIngrese la longitud de la contraseña mínimo 8 caracteres: ")

        if longitud.isdigit():
            longitud = int(longitud)

            if longitud >= 8:
                break
            else:
                print("ERROR: La contraseña debe tener mínimo 8 caracteres.")
        else:
            print("ERROR: Solo debe ingresar números.")

    while True:
        usar_mayusculas = input("¿Desea usar MAYÚSCULAS? (s/n): ").lower()
        usar_minusculas = input("¿Desea usar minúsculas? (s/n): ").lower()
        usar_numeros = input("¿Desea usar números? (s/n): ").lower()
        usar_simbolos = input("¿Desea usar símbolos? (s/n): ").lower()

        if (usar_mayusculas not in ["s", "n"] or
            usar_minusculas not in ["s", "n"] or
            usar_numeros not in ["s", "n"] or
            usar_simbolos not in ["s", "n"]):
            print("ERROR: Solo debe responder con 's' para sí o 'n' para no.")
            continue

        caracteres = ""
        obligatorios = []
        tipos_seleccionados = 0

        if usar_mayusculas == "s":
            caracteres += string.ascii_uppercase
            obligatorios.append(secrets.choice(string.ascii_uppercase))
            tipos_seleccionados += 1

        if usar_minusculas == "s":
            caracteres += string.ascii_lowercase
            obligatorios.append(secrets.choice(string.ascii_lowercase))
            tipos_seleccionados += 1

        if usar_numeros == "s":
            caracteres += string.digits
            obligatorios.append(secrets.choice(string.digits))
            tipos_seleccionados += 1

        if usar_simbolos == "s":
            caracteres += string.punctuation
            obligatorios.append(secrets.choice(string.punctuation))
            tipos_seleccionados += 1

        if tipos_seleccionados == 0:
            print("ERROR: Debe seleccionar al menos un tipo de carácter.")
        else:
            break

    contraseña = obligatorios.copy()

    for i in range(longitud - len(obligatorios)):
        contraseña.append(secrets.choice(caracteres))

    secrets.SystemRandom().shuffle(contraseña)

    contraseña = "".join(contraseña)

    puntaje = 0

    if longitud >= 8:
        puntaje += 1
    if longitud >= 12:
        puntaje += 1
    if tipos_seleccionados >= 2:
        puntaje += 1
    if tipos_seleccionados >= 3:
        puntaje += 1
    if tipos_seleccionados == 4:
        puntaje += 1

    if puntaje <= 2:
        nivel = "DÉBIL"
        recomendacion = "Use una contraseña más larga y combine más tipos de caracteres."
    elif puntaje == 3:
        nivel = "MEDIA"
        recomendacion = "La contraseña es aceptable, pero puede mejorar usando más longitud o más tipos de caracteres."
    elif puntaje == 4:
        nivel = "FUERTE"
        recomendacion = "La contraseña tiene un buen nivel de seguridad."
    else:
        nivel = "MUY FUERTE"
        recomendacion = "Excelente. La contraseña combina diferentes tipos de caracteres y una longitud adecuada."

    print("RESUMEN DE CONFIGURACIÓN")
    print("Longitud seleccionada :", longitud)
    print("Mayúsculas            :", "Sí" if usar_mayusculas == "s" else "No")
    print("Minúsculas            :", "Sí" if usar_minusculas == "s" else "No")
    print("Números               :", "Sí" if usar_numeros == "s" else "No")
    print("Símbolos              :", "Sí" if usar_simbolos == "s" else "No")

    print("CONTRASEÑA GENERADA:")
    print(contraseña)

    print("\nNivel de seguridad", nivel)
    print("\nRecomendación:")
    print(recomendacion)

    repetir = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

    if repetir != "s":
        print("\n==========================================")
        print("Gracias por utilizar el Generador Seguro de Contraseñas.")
        print("Hasta pronto.")
        break