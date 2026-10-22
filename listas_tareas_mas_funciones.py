# ==============================================================
# MINI PROYECTO EVOLUCIONADO: Lista de Tareas con Funciones
# Dia 8 - Funciones (def)
# ==============================================================
#
# ¿QUE CAMBIO RESPECTO A LA VERSION ANTERIOR?
# En vez de tener todo el codigo amontonado dentro del "while",
# ahora dividimos cada accion en una "cajita de herramientas" (una funcion).
#
# Cada funcion hace UNA sola cosa bien hecha:
# 1. mostrar_menu()   -> Muestra las opciones en pantalla
# 2. ver_tareas()     -> Muestra la lista de tareas
# 3. agregar_tarea()  -> Pide una tarea nueva y la guarda
# 4. eliminar_tarea() -> Pregunta cual borrar y la saca de la lista
# ==============================================================


# --------------------------------------------------------------
# FUNCION 1: Mostrar el menu
# --------------------------------------------------------------
# "def" le dice a Python: "aprendete esta receta con este nombre".
# Los parentesis vacios () significan que no necesita ningun ingrediente extra.
def mostrar_menu():
    """Esta funcion solo imprime las opciones disponibles."""
    print("\nQue queres hacer?")
    print("1. Ver mis tareas")
    print("2. Agregar una tarea")
    print("3. Eliminar una tarea")
    print("4. Salir")


# --------------------------------------------------------------
# FUNCION 2: Ver las tareas
# --------------------------------------------------------------
# Fijate que dentro de los parentesis pusimos "(lista)".
# Eso es un "parametro" o ingrediente: la funcion necesita que le pasemos
# la lista de tareas para poder revisarla e imprimirla.
def ver_tareas(lista):
    """Muestra todas las tareas que hay en la lista numeradas."""
    # len(lista) cuenta cuantas cosas hay adentro
    if len(lista) == 0:
        print("\n[OK] No tenes tareas pendientes. Estas al dia!")
    else:
        print("\n--- Tus tareas ---")
        # enumerate le coloca el numerito 1, 2, 3... al lado de cada tarea
        for numero, tarea in enumerate(lista, 1):
            print(f"  {numero}. {tarea}")
        print("-" * 30)


# --------------------------------------------------------------
# FUNCION 3: Agregar una tarea
# --------------------------------------------------------------
# Tambien recibe la "lista" como ingrediente para meterle la nueva tarea.
def agregar_tarea(lista):
    """Pide al usuario una nueva tarea y la agrega a la lista."""
    nueva_tarea = input("Escribi la nueva tarea: ")

    # Validacion: evitar que agreguen texto vacio o solo espacios
    if nueva_tarea.strip() == "":
        print("[!] No podes agregar una tarea vacia, parce.")
    else:
        # .append() mete el elemento al final de la bolsa
        lista.append(nueva_tarea)
        print(f"[+] Tarea '{nueva_tarea}' agregada con exito.")


# --------------------------------------------------------------
# FUNCION 4: Eliminar una tarea
# --------------------------------------------------------------
def eliminar_tarea(lista):
    """Muestra las tareas actuales y elimina la que el usuario elija."""
    if len(lista) == 0:
        print("\n[!] No hay tareas para eliminar.")
        return  # "return" solito sirve para salir de la funcion de una vez

    # Reutilizamos la funcion ver_tareas para que el usuario vea que numeros hay
    ver_tareas(lista)

    numero_borrar = input("Cual queres eliminar? (escribi el numero): ")

    # Validacion: comprobar que el usuario de verdad escribio un numero
    if numero_borrar.isdigit():
        numero_borrar = int(numero_borrar)

        # Validacion: que el numero este entre 1 y el total de tareas
        if 1 <= numero_borrar <= len(lista):
            # .pop() saca el elemento de la lista usando su posicion (restando 1)
            tarea_eliminada = lista.pop(numero_borrar - 1)
            print(f"[-] Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("[!] Ese numero no existe en tu lista.")
    else:
        print("[!] Eso no es un numero valido, parce.")


# ==============================================================
# PROGRAMA PRINCIPAL (Donde arranca la accion)
# ==============================================================
# Aca creamos la lista real en memoria donde se guardaran las tareas
tareas = []

print("=" * 40)
print("  >> MI LISTA DE TAREAS (CON FUNCIONES) <<")
print("=" * 40)

# Bucle infinito para mantener el programa activo hasta elegir opcion 4
while True:
    # 1. Llamamos a la funcion que muestra el menu
    mostrar_menu()

    # 2. Pedimos la decision del usuario
    opcion = input("\nEligi una opcion (1-4): ")

    # 3. Segun la opcion, llamamos a la funcion encargada
    if opcion == "1":
        ver_tareas(tareas)

    elif opcion == "2":
        agregar_tarea(tareas)

    elif opcion == "3":
        eliminar_tarea(tareas)

    elif opcion == "4":
        print("\nNos vemos, parcero! Que descanses.")
        break  # Rompe el bucle y cierra el programa

    else:
        print("[!] Opcion no valida. Elegi entre 1 y 4.")
