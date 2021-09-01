data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(b)


## leer bytearray
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
    
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))



# ingresa aquí el código que lee los bytes del stream

