class MyZeroDivisionError(ZeroDivisionError):	
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("peores noticias")
	else:		
		raise ZeroDivisionError("malas noticias")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('División entre cero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('Mi división entre cero')
	except ZeroDivisionError:
		print('División entre cero original')


######### CREAR UNA ESTRUCTURA PROPIA DE EXCEPCIONES ##########
class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def makePizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no hay tal pizza en el menú")
	if queso > 100:
		raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
	print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)