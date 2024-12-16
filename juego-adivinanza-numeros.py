import random


def juego_adivinanza():
    # Generar un número del 1 al 100
    numero_secreto = random.randint(1, 100) #randint indica que sea entero
    intentos = 0
    adivinado = False

    # Primeras líneas del juego donde se da la bienvenida
    print("¡Bienvenido al juego Adivina un número!!!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡Gana quien lo consigue con menos intentos!")

    while not adivinado:
        # Solicitar un número del 1 al 100
        adivinanza = input("Por favor, introduce un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Casting - Lo estamos pasando de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es aún mayor que {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor que {adivinanza}")
            else:
                print(
                    f"¡Adivinado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos."
                    
                )
                adivinado = True  # Marcar como adivinado para salir del bucle
        else:
            print("Recuerda qu etiene que ser un número válido entre el 1 al 100")

# Una vez que termina un juego, le preguntamos si quiere seguir jugando
    jugar_de_nuevo = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
    if jugar_de_nuevo == 'sí':
        juego_adivinanza()
    else:
        if jugar_de_nuevo == 'no':
            print("Cuando te apetezca, volvemos a jugar")
        else:
            print(f"Como has dicho {jugar_de_nuevo}, entiendo que quieres decir no. Así que, hasta la próxima")

juego_adivinanza()

