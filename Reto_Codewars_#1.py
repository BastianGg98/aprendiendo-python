def filtrar_mayores():
    admitidos = []
    while True:
        # 1. Primero recibimos el TEXTO tal cual (sin int todavía)
        entrada = input("Ingrese una edad (o 'salir' para terminar): ")
        # 2. Revisamos si escribió 'salir'
        if entrada.lower() == 'salir':
            break  # Se sale sin problema
        # 3. Si no dijo salir, AHORA SÍ lo convertimos a número
        edad = int(entrada)
        # 4. Evaluamos la edad
        if edad >= 18:
            admitidos.append(edad)
    return admitidos

print("Programa de filtrado de edades")
mayores = filtrar_mayores()
print("Edades mayores o iguales a 18:", mayores)