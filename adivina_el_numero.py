import random


secreto = random.randint(1,10)
intento = int(input("Ingresa un numero: "))

if intento == secreto:
    print("Acertaste!")
elif intento > secreto:
    print("Muy alto!")
else:
    print("Muy bajo!")
