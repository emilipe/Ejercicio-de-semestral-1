import math
print ("Bienvenido, que desea calcular ? un cilindro o un cono(presione c para cilindro o presione o para cono")
opcion= str(input())
opcion=opcion.lower()

if opcion== "c":
    radioc=int(input ("Ingrese el radio del cilindro"))
    radioc=round(radioc,2)
    alturac=int(input("Ingrese la altura del cilindro"))
    alturac=round(alturac,2)
    volumenc=math.pi*(radioc**2)*alturac
    print (alturac)
    print (radioc)
    print ("El volumen del cilindro es", round(volumenc,2))
elif opcion=="o":
    radioD=int (input ("Ingrese el radio del cono"))
    radioD=round(radioD,2)
    alturaD=int(input ("Ingrese la altura del cono"))
    alturaD=round (alturaD, 2)
    volumenD=(math.pi*(radioD**2)*alturaD)/3
    print (alturaD)
    print (radioD)
    print ("el volumen del cono es", round(volumenD,2))
else:
    print ("Dulce o truco")