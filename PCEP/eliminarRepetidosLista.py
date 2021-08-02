
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# copio lista
#
final = miLista[:]

print("Lista 'Final'", final)



vueltasI = 0
for i in final :
    vueltasI += 1
    
    print("Vueltas I:", vueltasI)
    print("I:", i)

    for j in final[i+1:] :
        if i == j :
            print("Coincidencia, j =", j)
            
            del final[j]

print("La lista solo con elementos únicos:")
print(final)


## Con not in funciona

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# copio lista

#creo una lista nueva para ir añadiendo
final = []


#vueltasI = 0
for i in miLista :
   if i not in final :
       final.append(i)

print("La lista solo con elementos únicos:")
print(final)