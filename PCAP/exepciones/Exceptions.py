try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")

#Si deseas manejar dos o mas excepciones de la misma manera, puedes usar la siguiente sintaxis:

#try:
#    :
#except (exc1, exc2):
#    :



######### RAISE ##########
#La instrucción raise genera la excepción especificada denominada exc como si fuese generada de manera natural: EJEMPLO
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

######## ELSE & FINALLY ########
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))


######### EXCEPTION GENERAL PARA QUE NOS DÉ EL ERROR #########
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))
