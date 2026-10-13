
cuenta = float(input("Ingresa el valor de la cuenta: "))
porcentaje = float(input("Ingresar el porcentaje de la propina: "))

factor = porcentaje / 100
propina = cuenta * factor
total = cuenta + propina

print("el total de la cuenta a pagar: ", total)