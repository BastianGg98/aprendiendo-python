Op = int(input("Elige una opción: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n"))

match Op:
    case 1:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print("El resultado es: ", resultado)
    case 2:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 - num2 
        print("El resultado es: ", resultado)
    case 3:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print("El resultado es: ", resultado)
    case 4:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        resultado = "No se puede dividir entre cero" if num2 == 0 else num1 / num2
        print("El resultado es: ", resultado)
