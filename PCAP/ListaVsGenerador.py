lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()


## Los corchetes hacen una comprensión, los paréntesis hacen un generador.

#¿Cómo puedes saber que la segunda asignación crea un generador, no una lista?
# pruebas que podemos mostrarte. Aplica la función len() a ambas entidades.
# len(lst) dará como resultado 10, claro y predecible, len(genr) provocará una excepción y verás el siguiente mensaje:
# TypeError: object of type 'generator' has no len()