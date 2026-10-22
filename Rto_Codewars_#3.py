lista = []

def promedio (lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def nota_mas_alta (lista):
    if len(lista) == 0:
        return None
    return max(lista)

def nota_mas_baja (lista):
    if len(lista) == 0:
        return None
    return min(lista)

def aprobados (lista):
    if len(lista) == 0:
        return 0
    return len([nota for nota in lista if nota >= 6])

def reprobados (lista):
    if len(lista) == 0:
        return 0
    return len([nota for nota in lista if nota < 6])


print("=" * 40)
print("EL PROGRAMA DEL PROFE")
print("=" * 40)

while True:
    entrada = input("Ingrese una nota o 'salir' para terminar: ")
    if entrada.lower() == 'salir':
        break
    entrada = int(entrada)
    if entrada < 0 or entrada > 10:
        print("Nota inválida. Debe estar entre 0 y 10.")
        continue
    lista.append(entrada)

print("Promedio de notas:", promedio(lista))
print("Nota más alta:", nota_mas_alta(lista))
print("Nota más baja:", nota_mas_baja(lista))
print("Cantidad de aprobados:", aprobados(lista))
print("Cantidad de reprobados:", reprobados(lista))





