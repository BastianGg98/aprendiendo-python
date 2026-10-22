import os
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = os.path.join(carpeta_actual, "Mis Notas#2.txt")
3
if not os.path.exists(nombre_archivo):
    open(nombre_archivo, "w", encoding="utf-8").close()

def mostrar_menu():
    print("\n[1] Ver tareas")
    print("[2] Agregar tarea")
    print("[3] Eliminar tarea")
    print("[4] Salir")
    

def ver_tareas():
    if not os.path.exists(nombre_archivo):
        print("\n[!] No existe tal archivo.")
    else:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            tareas = archivo.readlines()
            if len(tareas) == 0:
                print ("\n[!] no hay tareas guardadas.")
            else:
                print("\n--- Tus tareas ---")
                for linea in tareas:
                    print(linea.strip())

def agregar_tarea():
    nueva_tarea = input("Escriba la nueva tarea: ")
    if nueva_tarea.strip() == "":
        print("[!] No se puede agregar una tarea vacía.")
    else:
        with open(nombre_archivo, "a", encoding = "utf-8") as archivo:
            archivo.write(nueva_tarea + "\n")
        print(f"[+] Tarea '{nueva_tarea}' agregada con éxito.")

def eliminar_tarea():
    if not os.path.exists(nombre_archivo):
        print("\n[!] No existe tal archivo.")
    else:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            tareas = archivo.readlines()
            if len(tareas) == 0:
                print("\n[!] No hay tareas para eliminar.")
            else:
                print("\n --- Tus tareas ---")
                for i, tarea, in enumerate(tareas,1):
                    print(f"{i}. {tarea.strip()}")
                try:
                    indice = int(input("Ingrese el número de la tarea a eliminar: "))
                    if 1 <= indice <= len(tareas):
                        tareas.pop(indice - 1)
                        with open(nombre_archivo, "w", encoding = "utf-8") as archivo:
                            archivo.writelines(tareas)
                        print(f"[+] Tarea eliminada con éxito.")
                    else:
                        print("[!] Índice inválido.")
                except ValueError:
                    print("[!] Por favor, ingrese un número válido.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("[!] Opción inválida. Intente nuevamente.")


