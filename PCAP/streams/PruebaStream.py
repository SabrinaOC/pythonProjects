# vas a copiar el contenido del archivo a la consola y contarás todos los caracteres que el programa ha leído.

from os import strerror

def leer (s):
    for i in s.read():
        #cont +=1
        print(i, end='')

#def leerYContarLetra(st, letra):
    
def cantidadLetras(st, letra):
    contLetra = 0
    for i in st.read():
        if i == letra:
            contLetra += 1
    return i + "->" + contLetra
    #return cantidadLetras

try:
    stream = open("C:\\Users\\Sabri\\leerPython.txt", "r+", encoding="utf-8") 

    

  
    #cont = 0
    #for i in stream.read():
    #    cont +=1
     #   print(i, end='')
    leer(stream)

    #stream.write("\n" + input("\nAñade una línea al texto:"))

    cantidadLetras(stream, input("elige una letra para contar: "))

    

    stream.close()
except Exception as exc:
    print("El archivo no se pudo abrir:", strerror(exc.errno))


