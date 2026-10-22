# ==============================================================
# RETO 2 (Logica): El cajero del D1 / Cuenta la plata
# Resuelto por: Bastian
# ==============================================================

def totalizar():
    items = []
    while True:
        entrada = input("Ingrese el precio del producto (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            break
        numero = float(entrada)
        items.append(numero)
        
    total = sum(items)
    cantidad = len(items)
    
    # Devolvemos ambas variables al mismo tiempo
    return total, cantidad

print("=" * 40)
print("  🛒 CAJERO REGISTRADOR D1")
print("=" * 40)

# Recibimos ambos valores devueltos por la funcion
total_pagar, total_productos = totalizar()

print("\n--- 🧾 Resumen de tu compra ---")
print(f"Cantidad de items: {total_productos}")
print(f"Total a pagar: ${total_pagar}")
print("=" * 40)
