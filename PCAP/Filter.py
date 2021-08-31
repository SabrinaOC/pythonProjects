from random import seed, randint

##  filtra su segundo argumento mientras es guiado por direcciones que fluyen desde la función especificada en el primer argumento
# Los elementos que regresan True de la función pasan el filtro - los otros son rechazados.


seed()
data = [ randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)