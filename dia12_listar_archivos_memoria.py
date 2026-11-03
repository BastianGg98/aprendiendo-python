import os
carpeta_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = os.path.join(carpeta_actual, "servidor_accesos.log")

if not os.path.exists(nombre_archivo):
    open(nombre_archivo, "w", encoding="utf-8").close()

def ver_logs():
    if not os.path.exists(nombre_archivo):
        print("\n[!] No existe tal archivo.")
    else:
        with open(nombre_archivo, "r", encoding = "utf-8") as archivo:
            logs = archivo.readlines()
            if len(logs) == 0:
                print ("\n[!] no hay logs guardados.")
            else:
                print("\n--- Logs de accesos ---")
                bloqueados = []
                intentos_fallidos = 0
                for linea in logs:
                    if "FAILED" in linea:
                        partes = linea.split()
                        ip = partes[2]
                        intentos_fallidos += 1
                        bloqueados.append(ip)
                        print(f"[ALERTA] Intento fallido desde la IP: {ip}")
                print(f"[INFO] Total de intentos fallidos: {intentos_fallidos}")
                archivo_salida = os.path.join(carpeta_actual, "ips_bloqueadas.txt")
                with open(archivo_salida, "a", encoding="utf-8") as salida:
                    for una_ip in bloqueados:
                        salida.write(una_ip + "\n")
                print(f"[OK] Reporte guardado con exito en ips_bloqueadas.txt")
                        
ver_logs()
