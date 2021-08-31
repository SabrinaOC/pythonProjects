class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()    # instanciando el objeto



#Creación subclase
class SumarPila(Pila):
    def __init__(self):
        # Python obliga a llamar al constructor de la superclase
        Pila.__init__(self)
        self.__sum = 0

    ##sobreescribir métodos de superclase

##  Tenemos que especificar el nombre de la superclase; 
# esto es necesario para indicar claramente la clase que contiene el método, 
# para evitar confundirlo con cualquier otra función del mismo nombre.
##Tenemos que especificar el objeto de destino y pasarlo como primer argumento 
# (no se agrega implícitamente a la invocación en este contexto).

    def push(self, val):
        Pila.push(self, val)
        self.__sum += val


##GETTERS y SETTERS
    def getSuma(self):
        return self.__sum
