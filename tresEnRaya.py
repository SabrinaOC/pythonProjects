#imports
from random import randrange

#Variables necesarias juego

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
ganador = False
movimiento = 1
turno = False # f --> máquina // t --> jugador
ganador = False
libres = True




def DisplayBoard(board):
    #
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola

    print("Tablero actual:")

    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="\t")
            
        print()

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    vacio = False
#Bucle hasta que ingrese posición correcta
    while vacio != True:

        ubi = int(input("Ingresa posición próxima jugada:"))
        vacio = ComprobarDisponibilidad(board, "O", ubi)
        if vacio != True :
                print("Casilla no disponible, elige otra")
    
    DisplayBoard(board)

def VictoryFor(board):
#Recorremos listas para ver ganador
    #1 filas
    for i in range(len(board)):
            #for j in range(len(board[i])):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] :
                if board[i][0] == "X":
                    print("La máquina ha ganado")
                else:
                    print("¡Los humanos ganan!")
                return True
            
    #2 columnas
    #for i in range(len(board)):
    for i in range(len(board[0])):
        #print("Comprobación columnas i=", i)
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == "X":
                print("La máquina ha ganado")
            else:
                print("¡Los humanos ganan!")
            return True
        
    #3 diagonal principal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] :
        if board[0][0] == "X":
            print("La máquina ha ganado")
        else:
            print("¡Los humanos ganan!")
        return True
    
    #4 diagonal secundaria
    if board [0][2] == board [1][1] and board [0][2] == board [2][0] :
        if board[0][2] == "X":
            print("La máquina ha ganado")
        else:
            print("¡Los humanos ganan!")
        return True


def DrawMove(board, movimiento):
    #Si es el primer movimiento tiene que ser una X en 5
    if movimiento == 1 :
        for i in range(len(board)):
            for j in range(len(board[i])):

                if board[i][j] == "5" :
                    #Después de mostrarlo en pantalla cambio la lista para conservar cambios
                    board[i][j] = "X"
        DisplayBoard(board)
    else :
        #Si no es el primer movimiento lanzo un número al azar para posición X
        #Variable para bucle numeros aleatorios hasta encontrar vacío
        vacio = False
        while vacio != True:
            #lanzamos random
            ubi = randrange(9)

            vacio = ComprobarDisponibilidad(board, "X", ubi)
            
        #Cuando nos aseguramos que está vacío pintamos en pantalla
        DisplayBoard(board)

# Función para comprobar disponibilidad
def ComprobarDisponibilidad(board, jugador, posicion):

    for i in range(len(board)):
        for j in range(len(board[i])):
            #cuando el random coincida con num tendremos coordenadas
            if board[i][j] == str(posicion):
                #print("Posición insertada:", posicion)
                if board[i][j] != "X" and board[i][j] != "O":
                    #Después de comprobar disponibilidad pintamos en pantalla el jugador correspondiente
                    board[i][j] = jugador
                    #devolvemos true o false para salir de bucle método principal
                    #print("Devuelvo true disponible")
                    return True

def EspaciosLibres (board):
    #Recorremos listas para ver si hay huecos disponibles para seguir jugando
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "O":
                return True


DisplayBoard(board)
while ganador != True and libres:
    
    if turno :
        EnterMove(board)
        #Comprobamos ganador
        ganador = VictoryFor(board)
        #Después de la jugada cambiamos turno
        turno = False
    else:
        DrawMove(board, movimiento)
        #Comprobamos ganador
        ganador = VictoryFor(board)
        #Después de la jugada cambiamos turno y sumamos movimiento
        turno = True
        movimiento += 1
    #comprobamos si sigue habiendo espacios libres
    libres = EspaciosLibres(board)
    if libres != True and ganador != True:
        print("¡Empate! No se pueden colocar más fichas")


