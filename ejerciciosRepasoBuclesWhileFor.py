#1. 0-10 con for mostrando impares
print("Ejercicio 1")
for i in range(11) :
    if i % 2 != 0 :
        print (i)

#2. Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
print("\nEjercicio 2")
i = 0
while i<11 :
    if i % 2 != 0 :
        print (i)
    i += 1

#3. Crea un programa con un bucle for y una declaración break.
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.
print("\nEjercicio 3")
email = input("Ingrese su correo electrónico: ")
salida = ""

for i in email :
    if i == "@" :
        break
    salida += i

print(salida)

#4. Crea un programa con un bucle for y una declaración continue.
# El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
print("\nEjercicio 4")
sal = ""

for digit in "0165031806510":
    if digit == "0":
        continue
    sal += digit

print (sal)
