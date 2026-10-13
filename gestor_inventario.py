import json
import os
import datetime

ARCHIVO = "inventario.json"
usuarios = {"admin": "admin123", "ventas": "ventas2024"}


def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return {"productos": {}, "ventas": []}
    with open(ARCHIVO, "r") as f:
        return json.load(f)


def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)


def login():
    intentos = 0
    while True:
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        if usuario in usuarios and usuarios[usuario] == clave:
            print("Bienvenido", usuario)
            return usuario
        intentos += 1
        print("Credenciales incorrectas, intentos:", intentos)


def agregar_producto(datos):
    nombre = input("Nombre del producto: ").strip().lower()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    if nombre in datos["productos"]:
        datos["productos"][nombre]["cantidad"] += cantidad
    else:
        datos["productos"][nombre] = {"precio": precio, "cantidad": cantidad}
    guardar_datos(datos)
    print("Producto guardado")


def listar_productos(datos):
    if not datos["productos"]:
        print("No hay productos")
        return
    print("PRODUCTO | PRECIO | STOCK")
    for nombre, info in datos["productos"].items():
        print(nombre, "|", info["precio"], "|", info["cantidad"])


def vender(datos, usuario):
    nombre = input("Producto a vender: ").strip().lower()
    if nombre not in datos["productos"]:
        print("Producto no existe")
        return
    cantidad = int(input("Cantidad: "))
    producto = datos["productos"][nombre]
    if cantidad > producto["cantidad"]:
        print("Stock insuficiente")
        return
    descuento = int(input("Descuento (%): "))
    total = producto["precio"] * cantidad
    total = total - (total * descuento / 100)
    producto["cantidad"] -= cantidad
    datos["ventas"].append({
        "producto": nombre,
        "cantidad": cantidad,
        "total": total,
        "vendedor": usuario,
        "fecha": str(datetime.date.today()),
    })
    guardar_datos(datos)
    print("Venta registrada. Total:", total)


def eliminar_producto(datos, usuario):
    if usuario == "admin" or usuario:
        nombre = input("Producto a eliminar: ").strip().lower()
        if nombre in datos["productos"]:
            del datos["productos"][nombre]
            guardar_datos(datos)
            print("Producto eliminado")
        else:
            print("Producto no existe")
    else:
        print("No tienes permiso")


def exportar_reporte(datos):
    nombre_archivo = input("Nombre del archivo de reporte: ")
    total_ventas = 0
    for venta in datos["ventas"]:
        total_ventas += venta["total"]
    with open(nombre_archivo + ".txt", "w", encoding="utf-8") as f:
        f.write(f"Total vendido: {total_ventas}\n")
    print("Reporte exportado")


def menu():
    usuario = login()
    datos = cargar_datos()
    while True:
        print("\n1. Agregar producto")
        print("2. Listar productos")
        print("3. Vender")
        print("4. Eliminar producto")
        print("5. Exportar reporte")
        print("0. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            agregar_producto(datos)
        elif opcion == "2":
            listar_productos(datos)
        elif opcion == "3":
            vender(datos, usuario)
        elif opcion == "4":
            eliminar_producto(datos, usuario)
        elif opcion == "5":
            exportar_reporte(datos)
        elif opcion == "0":
            print("Hasta luego")
            break
        else:
            print("Opcion invalida")


menu()
