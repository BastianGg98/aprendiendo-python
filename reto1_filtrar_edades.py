# ==============================================================
# RETO 1 (Logica): El portero de la discoteca
# Resuelto por: Bastian
# ==============================================================

def filtrar_mayores():
    admitidos = []
    while True:
        entrada = input("Ingrese una edad (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        edad = int(entrada)
        if edad >= 18:
            admitidos.append(edad)
    return admitidos

print("=" * 40)
print("  Programa de filtrado de edades")
print("=" * 40)
mayores = filtrar_mayores()
print("\n[+] Edades mayores o iguales a 18:", mayores)
