import math
respuesta=input ("Sea bienvenido, Deseas empezar el programa?")
respuesta=respuesta.lower()
while respuesta=="si":
    a=int(input ('ingresa el valor de A'))
    b=int (input ('ingresa el valor de B'))
    c=int(input ('ingresa el valor de C'))
    B=b*b 
    discriminante=B-(4*a*c)
    
    if discriminante>=0:
        discriminante=math.sqrt(discriminante)
        x1=-b-discriminante/(2*a)
        x2=-b+discriminante/(2*a)
        print ("Los valores de la raices son x1 =",x1,"x2 =",x2)
        print("Ecuacion factorizada (x- ",x1,")*(x- ",x2,")")
    else:
        print("discriminante negativo, raices imaginarias")
    print("desea continuar con el programa ?")