#import sys
#from typing import colored, cprint

#import colorama
#from colorama import init
# use Colorama to make Termcolor work on Windows too
#init()
from colorama import Fore as letra, Back as fondo, Style as estilo
print(letra.RED +  fondo.WHITE + estilo.BRIGHT + 'some red text en fondo blanco' + estilo.RESET_ALL )

print("Cambiando colores con ANSI")
print("\033[0;31m" + "esto es color rojo. Normal " + "\033[0m")
print("\033[1;32m" + "esto es color verde. Bold" + "\033[0m")
print("\033[2;33m" + "esto es color amarillo. Light " + "\033[0m")
print("\033[3;34m" + "esto es color azul. Italics " + "\033[0m")
print("\033[4;35m" + "esto es color morado. Subrayado " + "\033[0m")
print("\033[5;36m" + "esto es color cyan." + "\033[0m")
print("\033[0;37;40m" + "esto es color blanco. " + "\033[0m")

print("\nCambiando fondos con ANSI")
print("\033[0;37;41m" + "esto es color rojo. " + "\033[0m")
print("\033[1;37;42m" + "esto es color verde. Bold" + "\033[0m")
print("\033[1;37;43m" + "esto es color amarillo " + "\033[0m")
print("\033[1;37:44m" + "esto es color azul " + "\033[0m")
print("\033[1;37;45m" + "esto es color morado " + "\033[0m")
print("\033[1;37;46m" + "esto es color cyan " + "\033[0m")
print("\033[1;30;47m" + "esto es color blanco " + "\033[0m")

#print("\033[4;31m" + "hello " + "red")
#print("\033[0;37m")