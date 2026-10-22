def totalizar():
    items = []
    while True:
        entrada = input("Ingrese un número (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            break
        numero = float(entrada)
        items.append(numero)

        total = sum(items)
        cantidad = len(items)
    return total, cantidad

total_pagar, total_productos = totalizar()
print("\n--- Resumen de tu compra ---")
print(f"Cantidad de items: {total_productos}")
print(f"Total a pagar: ${total_pagar}")