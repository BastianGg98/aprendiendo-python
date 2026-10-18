# ============================================
# MINI PROYECTO: Lista de Tareas en Consola
# Dia 6 - Listas y Diccionarios
# ============================================
#
# QUE HACE ESTE PROGRAMA:
# Te deja agregar, ver y eliminar tareas desde la terminal.
# Es como una app de notas pero en texto.
#
# CONCEPTOS QUE VAS A APRENDER ACA:
# - Listas (guardar varios datos en una sola variable)
# - .append() (agregar un dato a la lista)
# - .pop() (eliminar un dato de la lista por posicion)
# - len() (contar cuantos elementos tiene la lista)
# - enumerate() (recorrer la lista con un numero al lado)
# - while True + break (repetir algo hasta que el usuario decida parar)
# - input() (pedirle datos al usuario)
# - if / elif / else (tomar decisiones)
# ============================================


# ------------------------------------------
# PASO 1: Crear la lista vacia
# ------------------------------------------
tareas = []


# ------------------------------------------
# PASO 2: Mostrar el titulo del programa
# ------------------------------------------
print("=" * 40)
print("  >> MI LISTA DE TAREAS <<")
print("=" * 40)


# ------------------------------------------
# PASO 3: El bucle principal
# ------------------------------------------
while True:

    # Mostramos las 4 opciones del menu
    print("\nQue queres hacer?")
    print("1. Ver mis tareas")
    print("2. Agregar una tarea")
    print("3. Eliminar una tarea")
    print("4. Salir")

    opcion = input("\nEligi una opcion (1-4): ")


    # ==========================================
    # OPCION 1: VER TAREAS
    # ==========================================
    if opcion == "1":

        if len(tareas) == 0:
            print("\n[OK] No tenes tareas pendientes. Estas al dia!")
        else:
            print("\n--- Tus tareas ---")
            for numero, tarea in enumerate(tareas, 1):
                print(f"  {numero}. {tarea}")
            print("-" * 30)


    # ==========================================
    # OPCION 2: AGREGAR UNA TAREA
    # ==========================================
    elif opcion == "2":

        nueva_tarea = input("Escribi la nueva tarea: ")

        if nueva_tarea.strip() == "":
            print("[!] No podes agregar una tarea vacia, parce.")
        else:
            tareas.append(nueva_tarea)
            print(f"[+] Tarea '{nueva_tarea}' agregada.")


    # ==========================================
    # OPCION 3: ELIMINAR UNA TAREA
    # ==========================================
    elif opcion == "3":

        if len(tareas) == 0:
            print("\n[!] No hay tareas para eliminar.")
        else:
            print("\n--- Tus tareas ---")
            for numero, tarea in enumerate(tareas, 1):
                print(f"  {numero}. {tarea}")

            numero_borrar = input("Cual queres eliminar? (escribi el numero): ")

            if numero_borrar.isdigit():
                numero_borrar = int(numero_borrar)

                if 1 <= numero_borrar <= len(tareas):
                    tarea_eliminada = tareas.pop(numero_borrar - 1)
                    print(f"[-] Tarea '{tarea_eliminada}' eliminada.")
                else:
                    print("[!] Ese numero no existe en la lista.")
            else:
                print("[!] Eso no es un numero valido, parce.")


    # ==========================================
    # OPCION 4: SALIR DEL PROGRAMA
    # ==========================================
    elif opcion == "4":
        print("\nNos vemos, parcero! Que estes bien.")
        break


    # ==========================================
    # SI ESCRIBIO CUALQUIER OTRA COSA
    # ==========================================
    else:
        print("[!] Opcion no valida. Elegi entre 1 y 4.")
