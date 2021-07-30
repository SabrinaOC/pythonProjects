miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)

miLista2 = [8, 10, 6, 2, 4] # lista para ordenar
print(miLista2)

#método para odernar la lista de python
miLista2.sort()
print(miLista2)

#método para ordenar la lista al revés
miLista2.reverse()
print(miLista2)