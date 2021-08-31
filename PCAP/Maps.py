## Estructura: map(función, lista)
#La función map() aplica la función pasada por su primer argumento a todos los elementos de su segundo argumento
# y devuelve un iterador que entrega todos los resultados de funciones posteriores.
# Puedes usar el iterador resultante en un bucle o convertirlo en una lista usando la función list().


lista1 = [x for x in range(5)]
print(lista1)
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)