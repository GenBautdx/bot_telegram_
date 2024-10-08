import paramiko

# Configura tu conexión
hostname = '10.250.8.106'  #  la dirección de tu servidor
username = 'root'  # tu usuario
password = 'Passw0rd'  # tu contraseña

def ejecutar_comando(accion):
    # Crear un cliente SSH
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectar al servidor
        cliente.connect(hostname, username=username, password=password)
        print("Conexión exitosa")

        # Determinar el comando según la acción
        if accion == 'start':
            command = "sh /middleware/user_projects/domains/base_domain/sas_prod_domain/admin.sh start"
        elif accion == 'stop':
            command = "sh /middleware/user_projects/domains/base_domain/sas_prod_domain/admin.sh stop"
        else:
            print("Acción no válida. Usa 'start' o 'stop'.")
            return

        # Ejecutar el comando
        stdin, stdout, stderr = cliente.exec_command(command)

        # Leer la salida
        print("Salida:", stdout.read().decode())
        print("Error:", stderr.read().decode())

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        cliente.close()

# Ejemplo de uso
accion = 'start'  # Cambia a 'stop' para detener el servicio
ejecutar_comando(accion)
