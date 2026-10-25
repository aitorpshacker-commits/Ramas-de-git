import random


puntaje = 0

while True:
    guess = int(input("¿Cuál crees que es el número entre 1 y 10?"))
    numero = random.randint(1,10)

    if guess == numero:
        print("Has adivinado el número")
        puntaje += 1
    else:
        print("No lo adivinaste, ten más duerte la próxima")
        print("El número era:", numero)

    pregunta = input("¿Quieres dejar de jugar?")
    if pregunta == "si":
        print("Gracias por jugar, tu puntaje es:", puntaje, "puntos")
        break