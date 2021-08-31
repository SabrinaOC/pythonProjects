class ClaseUno:
    pass

class ClaseDos(ClaseUno):
    pass

##función integrada de python para ver si una clase es subclase de otra, 
#aquí veremos si claseUno es subclase de claseDos
issubclass(ClaseUno, ClaseDos)

##comprobar si una instancia pertenece a una clase en concreto
#isinstance(nombreObjeto, nombreClase)
obj = ClaseUno()

isinstance(obj, ClaseUno)

#El operador is verifica si dos variables (en este caso objetoUno y objetoDos) se refieren al mismo objeto.
obj1 = ClaseUno()
obj2 = ClaseDos()
obj3 = obj1
print(obj1 is obj3)