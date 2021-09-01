#El nombre de la función (open) habla por si mismo; si la apertura es exitosa, la función devuelve un objeto stream;
# de lo contrario, se genera una excepción (por ejemplo, FileNotFoundError si el archivo que vas a leer no existe).

#El primer parámetro de la función (file) especifica el nombre del archivo que se asociará al stream.

#El segundo parámetro (mode) especifica el modo de apertura utilizado para el stream;
# es una cadena llena de una secuencia de caracteres, y cada uno de ellos tiene su propio significado especial (más detalles pronto).

#El tercer parámetro (encoding) especifica el tipo de codificación (por ejemplo, UTF-8 cuando se trabaja con archivos de texto).

#La apertura debe ser la primera operación realizada en el stream.

stream = open(file, mode = 'r', encoding = None)


#Abriendo el stream por primera vez
#Imagina que queremos desarrollar un programa que lea el contenido del archivo de texto llamado: C:\Users\User\Desktop\file.txt.



try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # aqui se procesa el archivo
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)


### DIAGNOSTICANDO PROBLEMAS CON LOS STREAMS
try:
    s = open()# operaciones con streams
except IOError as exc:
    print(exc.errno)