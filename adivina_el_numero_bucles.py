import random

secreto = random.randint(1,10)
intentos = 0

while intentos <= 5:
        intentos += 1
        intento = int(input("Ingresa un numero: "))
        print("Intentos: ", intentos)
        if intento == secreto:
            print("Acertaste!")
            print("El numero secreto era: ", secreto)
            break
        elif intento > secreto:
            print("Muy alto!")
        else:
            print("Muy bajo!")
        if intentos == 5:
            print("Se acabaron los intentos")
            print("El numero secreto era: ", secreto)
            break