from personajes import Personaje

print("¡Bienvenido a Gran Fantasía!")
nombre_jugador = input("Por favor, indique el nombre de su personaje: ")
jugador = Personaje(nombre_jugador)
jugador.estado()
orco = Personaje("Orco")
probabilidad = jugador.probabilidad_ganar(orco)
opcion = Personaje.juego(probabilidad)

# Ejemplo de uso de la función comparar_personajes
# Llama al método comparar_personajes desde la instancia jugador
1

while True:
    if opcion == 1:
        jugador.ataque(probabilidad,orco)
        jugador.estado()
        orco.estado()
        probabilidad = jugador.probabilidad_ganar(orco)
        opcion = Personaje.juego(probabilidad)

    elif opcion == 2:
        print("Has huido. El orco ha quedado atrás.")
        break
    else:
         print("colocque una opcion valida")
         break
    
