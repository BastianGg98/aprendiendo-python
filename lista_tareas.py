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
# Esto es como tener una bolsa de mercado vacia.
# Todavia no tiene nada adentro, pero ahi vamos a ir metiendo tareas.
# Los corchetes [] significan "lista vacia".

tareas = []


# ------------------------------------------
# PASO 2: Mostrar el titulo del programa
# ------------------------------------------
# print() muestra texto en la pantalla.
# "=" * 40 repite el signo = cuarenta veces. Es solo pa' que se vea bonito.

print("=" * 40)
print("  >> MI LISTA DE TAREAS <<")
print("=" * 40)


# ------------------------------------------
# PASO 3: El bucle principal
# ------------------------------------------
# "while True" significa "repeti esto PARA SIEMPRE".
# El programa va a seguir mostrandote el menu una y otra vez
# hasta que vos escribas "4" (salir), que es donde usamos "break"
# para romper el bucle y que el programa termine.

while True:

    # Mostramos las 4 opciones del menu
    print("\nQue queres hacer?")       # \n = salto de linea (dejar un espacio arriba)
    print("1. Ver mis tareas")
    print("2. Agregar una tarea")
    print("3. Eliminar una tarea")
    print("4. Salir")

    # Le pedimos al usuario que escriba un numero del 1 al 4
    # Lo que el usuario escriba se guarda en la variable "opcion"
    opcion = input("\nEligi una opcion (1-4): ")


    # ==========================================
    # OPCION 1: VER TAREAS
    # ==========================================
    # Si el usuario escribio "1", entramos aca.

    if opcion == "1":

        # len(tareas) cuenta cuantos elementos tiene la lista.
        # Si tiene 0, es porque esta vacia (no hay tareas).
        if len(tareas) == 0:
            print("\n[OK] No tenes tareas pendientes. Estas al dia!")

        else:
            # Si hay tareas, las mostramos una por una
            print("\n--- Tus tareas ---")

            # enumerate(tareas, 1) hace algo bacano:
            # Recorre la lista Y al mismo tiempo le pone un numero a cada elemento.
            # El "1" le dice que empiece a contar desde 1 (no desde 0).
            #
            # Ejemplo: si tareas = ["Estudiar", "Hacer ejercicio"]
            # enumerate va a dar:
            #   numero=1, tarea="Estudiar"
            #   numero=2, tarea="Hacer ejercicio"

            for numero, tarea in enumerate(tareas, 1):
                # f"..." es un f-string: te deja meter variables dentro del texto
                # {numero} se reemplaza por el numero real (1, 2, 3...)
                # {tarea} se reemplaza por el nombre de la tarea
                print(f"  {numero}. {tarea}")

            print("-" * 30)


    # ==========================================
    # OPCION 2: AGREGAR UNA TAREA
    # ==========================================
    # "elif" es como decir "si no fue la opcion anterior, probemos con esta"

    elif opcion == "2":

        # Le pedimos al usuario que escriba la tarea nueva
        nueva_tarea = input("Escribi la nueva tarea: ")

        # .strip() le quita los espacios en blanco al inicio y al final.
        # Si despues de quitar espacios queda vacio (""), es que no escribio nada.
        # Esto es una validacion: verificar que el dato sea correcto antes de usarlo.
        if nueva_tarea.strip() == "":
            print("[!] No podes agregar una tarea vacia, parce.")

        else:
            # .append() agrega un elemento AL FINAL de la lista.
            # Es como meter un producto mas a la bolsa de mercado.
            # Si tareas era ["Estudiar"], despues del append queda:
            # ["Estudiar", "Hacer ejercicio"]
            tareas.append(nueva_tarea)
            print(f"[+] Tarea '{nueva_tarea}' agregada.")


    # ==========================================
    # OPCION 3: ELIMINAR UNA TAREA
    # ==========================================

    elif opcion == "3":

        # Primero verificamos que haya tareas para eliminar
        if len(tareas) == 0:
            print("\n[!] No hay tareas para eliminar.")

        else:
            # Mostramos las tareas para que el usuario sepa cual borrar
            print("\n--- Tus tareas ---")
            for numero, tarea in enumerate(tareas, 1):
                print(f"  {numero}. {tarea}")

            # Le pedimos el numero de la tarea que quiere borrar
            numero_borrar = input("Cual queres eliminar? (escribi el numero): ")

            # .isdigit() verifica si lo que escribio es un numero.
            # Si el usuario escribio "hola" en vez de "2", esto da False.
            # Es otra validacion para que el programa no se rompa.
            if numero_borrar.isdigit():

                # int() convierte el texto "2" al numero 2.
                # Recordá que input() siempre devuelve texto, no numeros.
                numero_borrar = int(numero_borrar)

                # Verificamos que el numero este en el rango correcto.
                # Si hay 3 tareas, el numero tiene que ser entre 1 y 3.
                # len(tareas) nos dice cuantas tareas hay.
                if 1 <= numero_borrar <= len(tareas):

                    # .pop(posicion) elimina el elemento en esa posicion Y te lo devuelve.
                    # Ojo: las listas empiezan en posicion 0, no en 1.
                    # Por eso restamos 1: si el usuario dijo "2", borramos posicion 1.
                    #
                    # Ejemplo: tareas = ["Estudiar", "Ejercicio", "Cocinar"]
                    # tareas.pop(1) elimina "Ejercicio" (posicion 1)
                    # y la lista queda: ["Estudiar", "Cocinar"]
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

        # "break" rompe el "while True" y el programa termina.
        # Sin este break, el menu se repetiria para siempre.
        break


    # ==========================================
    # SI ESCRIBIO CUALQUIER OTRA COSA
    # ==========================================
    # Si no fue ni 1, ni 2, ni 3, ni 4... caemos aca.
    # "else" es el ultimo recurso: "si ninguna de las anteriores se cumplio..."

    else:
        print("[!] Opcion no valida. Elegi entre 1 y 4.")