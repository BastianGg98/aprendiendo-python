# ==============================================================
# DIA 10: MANEJO DE ARCHIVOS EN PYTHON (.txt)
# ==============================================================
# En este script vamos a practicar los 3 modos basicos:
# 1. Modo "w" -> Escribir (crea el archivo o sobreescribe)
# 2. Modo "a" -> Agregar texto al final sin borrar nada
# 3. Modo "r" -> Leer el contenido guardado
# ==============================================================

import os

# Con esto nos aseguramos de que el archivo .txt se cree en la misma carpeta que este script
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = os.path.join(carpeta_actual, "mis_notas.txt")

print("=" * 45)
print("PASO 1: Creando y escribiendo en el archivo...")
print("=" * 45)

# Usamos 'w' para arrancar una hoja en blanco
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("1. Aprender a manejar archivos en Python con Mike\n")
    archivo.write("2. Repasar los comandos de Git\n")

print("[OK] ¡Archivo creado y primeras notas guardadas con exito!\n")


print("=" * 45)
print("PASO 2: Agregando una linea extra con modo 'a' (Append)...")
print("=" * 45)

# Usamos 'a' para pegar una nueva linea abajo sin borrar las anteriores
with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("3. Tomarme un buen tinto bien cargado\n")

print("[OK] ¡Nueva linea agregada sin borrar las anteriores!\n")


print("=" * 45)
print("PASO 3: Leyendo lo que quedo en el archivo con modo 'r'...")
print("=" * 45)

# Usamos 'r' para abrir el cuaderno y chismosear lo que hay
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("El contenido de tu archivo en disco es:\n")
print(contenido)
print("=" * 45)
print("¡Listo el pollo! Persistencia de datos aprendida.")
print("=" * 45)
