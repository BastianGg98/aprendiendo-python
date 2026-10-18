# ==============================================================
# MINI PROYECTO EVOLUCIONADO: Lista de Tareas con Funciones
# Dia 8 - Funciones (def)
# ==============================================================

def mostrar_menu():
    """Esta funcion solo imprime las opciones disponibles."""
    print("\nQue queres hacer?")
    print("1. Ver mis tareas")
    print("2. Agregar una tarea")
    print("3. Eliminar una tarea")
    print("4. Salir")


def ver_tareas(lista):
    """Muestra todas las tareas que hay en la lista numeradas."""
    if len(lista) == 0:
        print("\n[OK] No tenes tareas pendientes. Estas al dia!")
    else:
        print("\n--- Tus tareas ---")
        for numero, tarea in enumerate(lista, 1):
            print(f"  {numero}. {tarea}")
        print("-" * 30)


def agregar_tarea(lista):
    """Pide al usuario una nueva tarea y la agrega a la lista."""
    nueva_tarea = input("Escribi la nueva tarea: ")
    if nueva_tarea.strip() == "":
        print("[!] No podes agregar una tarea vacia, parce.")
    else:
        lista.append(nueva_tarea)
        print(f"[+] Tarea '{nueva_tarea}' agregada con exito.")


def eliminar_tarea(lista):
    """Muestra las tareas actuales y elimina la que el usuario elija."""
    if len(lista) == 0:
        print("\n[!] No hay tareas para eliminar.")
        return

    ver_tareas(lista)
    numero_borrar = input("Cual queres eliminar? (escribi el numero): ")

    if numero_borrar.isdigit():
        numero_borrar = int(numero_borrar)
        if 1 <= numero_borrar <= len(lista):
            tarea_eliminada = lista.pop(numero_borrar - 1)
            print(f"[-] Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("[!] Ese numero no existe en tu lista.")
    else:
        print("[!] Eso no es un numero valido, parce.")


tareas = []

print("=" * 40)
print("  >> MI LISTA DE TAREAS (CON FUNCIONES) <<")
print("=" * 40)

while True:
    mostrar_menu()
    opcion = input("\nEligi una opcion (1-4): ")

    if opcion == "1":
        ver_tareas(tareas)
    elif opcion == "2":
        agregar_tarea(tareas)
    elif opcion == "3":
        eliminar_tarea(tareas)
    elif opcion == "4":
        print("\nNos vemos, parcero! Que descanses.")
        break
    else:
        print("[!] Opcion no valida. Elegi entre 1 y 4.")
