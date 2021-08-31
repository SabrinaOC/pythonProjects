class ClaseEjemplo:
    def __init__(self, val = 1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)

## Cuando Python ve que deseas agregar una variable de instancia a un objeto 
# y lo vas a hacer dentro de cualquiera de los métodos del objeto, maneja la operación de la siguiente manera:

#Coloca un nombre de clase antes de tu nombre.
#Coloca un guión bajo adicional al principio.
#Es por ello que __primera se convierte en _ClaseEjemplo__primera.

#El nombre ahora es completamente accesible desde fuera de la clase. Puedes ejecutar un código como este:

print(objetoEjemplo1._ClaseEjemplo__primera)