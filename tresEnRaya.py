#imports
from random import randrange

#Variables necesarias juego

board = [["1", "2", "3"], ["4", "1", "2"], ["0", "1", "2"]]
ganador = False
movimiento = 1
turno = False # f --> máquina // t --> jugador




def DisplayBoard(board):
    #
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola

    # Variable para mostrar en pantalla numeración tablero
    num = 1

    print("Tablero inicial:")

    for i in range(len(board)):

        for j in range(len(board[i])):
            #print ("""|""",   num  , """| """)
            print(num, end="\t")
            num += 1
        print()

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

    print("Juega jugador")

# def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

# def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#


def DrawMove(board, movimiento):
    #
    #  juega la maquina y actualiza el tablero
    #

    # creo el tablero una lista de tres elementos con listas dentro
    #Si es el primer movimiento tiene que ser una X en 5
    if movimiento == 1 :
        print("Jugada máquina. Movimiento:", movimiento)

        num = 1
        for i in range(len(board)):

            for j in range(len(board[i])):
                #print ("""|""",   num  , """| """)
                if num == 5 :
                    print("X", end="\t")
                    #Después de mostrarlo en pantalla cambio la lista para conservar cambios
                    board[i][j] = "X"
                else:
                    print(num, end="\t")
                num += 1
            print()
    else :
        #Si no es el primer movimiento lanzo un número al azar para posición X
        #Variable para bucle numeros aleatorios hasta encontrar vacío
        vacio = False
        while vacio == False:
            #lanzamos random
            ubi = randrange(9)

            #comprobamos que está vacío
            num = 1
            for i in range(len(board)):

                for j in range(len(board[i])):
                    #cuando el random coincida con num tendremos coordenadas
                    if num == ubi :
                        if board[i][j] != "X" and board[i][j] != "O":
                            #Después de comprobar disponibilidad pintamos en pantalla x
                            board[i][j] = "X"
                    
                

        #Cuando nos aseguramos que está vacío pintamos en pantalla




# print(type(ganador))
    #while ganador == False:
i = 0
DisplayBoard(board)
while i < 2 :
    
    if turno :
        EnterMove(board)
        #Después de la jugada cambiamos turno
        turno = False
    else:
        DrawMove(board, movimiento)
        #Después de la jugada cambiamos turno
        turno = True
    
    i += 1
print(board)