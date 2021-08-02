# imports
from random import randrange


# El programa te dice: elige el número de longitud de la cifra
# 3
# Por ejemplo
# El programa elige una cifra de tres cifras al azar
# Y tú tienes que adivinarlo
# Si lo adivinas, has ganado el juego
# Digamos que la cifra es 1 2 3
# Y tú dices 1 4 2
# Entonces el programa te dice que el uno lo has adivinado, y que luego hay una cifra incorrecta y una correcta pero mal posicionada

# Básicamente te respondería esto: 1 _ +
# La barra baja significa que esa cifra no está
# Y el más que esa cifra está, pero en otro lugar


# creamos lista
maquina = []

# Pedimos dimensiones de la lista al usuario
for i in range(int(input("¿Con cuántos números jugamos? "))):
    # damos valores aleatorios
    maquina.append(str(randrange(9)))
print()

# lista para guardar valores dados por el jugador
jugador = []


print("Ingresa un número del 0 al 9: ")
# para que tenga la misma dimensión usamos un for recorriendo la lista de la máquina
for i in range(len(maquina)):
    jugador.append(input())

print()

print("Números máquina:", maquina, "\nNúmeros jugador:", jugador)

print()

# ya tenemos las dos listas, ahora solo queda comparar
for i in range(len(maquina)):
    # si los valores de las dos listas en la misma posición son distintos, hacemos más comprobaciones
    if maquina[i] != jugador[i]:
        # recorro bucle de nuevo para comprobar si está en otra posición
        for j in range(len(maquina)):
            if jugador[i] == maquina[j]:
                # si encontramos coincidencia cambiamos lista y salimos de bucle
                jugador[i] = "+"
                break

            # si hemos recorrido la lista entera, es decir, estamos en la última posición 
            # y no hay + significa que ese número no está en la lista de la máquina
            elif j == len(maquina)-1 and jugador[i] != "+":
                jugador[i] = "_"


# finalmente imprimimos en pantalla los resultados
print("Números máquina:", maquina, "\nNúmeros jugador:", jugador)
