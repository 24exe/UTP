# Not my first contact, solo estoy recordando cosas.


nombre = input("¿Cuál es tu nombre? ")

print(f"Hola, {nombre}! bienvenid@ al programa. \n")
edad = int(input("¿Cuál es tu edad? "))
while edad <= 0:
    print ("ERROR, INGRESAR UNA EDAD ENTERA POSITIVA. \n")
    edad = int(input("¿Cuál es tu verdadera edad? "))

if edad <= 25:
    print(f"WOW {nombre},¿ {edad} años? que joven, bienvenid@. \n")
elif edad > 25 and edad <= 40:
    print(f"Me sorprendes {nombre}, en plena flor de la vida. \n")
else:
    print(f"Dicen que nunca es tarde para volver a empezar, ¿no {nombre}?")
