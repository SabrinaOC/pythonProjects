#pido número de bloques al usuario
bloques = int(input("Ingrese el número de bloques:"))

##variable contar pisos
altura = 0




print (bloques)
for i in range(1, bloques) :
    if i == 1 :
        altura = 1
        sumaBloques = 1

    if i == sumaBloques + 1:
        altura += 1
        sumaBloques += 1


print("La altura de la pirámide:", altura)