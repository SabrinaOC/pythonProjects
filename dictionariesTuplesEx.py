d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 =  {}

vueltas = 1
for elemento in (d1, d2):
    #print("Vueltas: ", vueltas)
    d3.update(elemento)
    vueltas += 1

print(d3, "vueltas:", vueltas)

l = ["carro", "Ford", "flor", "Tulipán"]

t = tuple(l)

print(t, type(t))

colores = (("verde", "#008000"), ("azul", "#0000FF"))

colDict = dict(colores)

print(type(colDict), colDict)