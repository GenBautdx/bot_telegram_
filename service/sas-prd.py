import paramiko
import time
import subprocess



# Configuración de conexión
hostname  = "10.250.8.106"  # Cambia esto por la dirección de tu servidor
username  = "root"
password  = "Passw0rd"

# Crear el cliente SSH
cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conectar al servidor
    cliente.connect(hostname, username=username, password=password)
    print("Conexión exitosa")

    # Ejecutar el comando
    command = "sh /middleware/user_projects/domains/base_domain/sas_prod_domain/admin.sh start"
    stdin, stdout, stderr = cliente.exec_command(command)

    # Leer la salida
    print("Salida:", stdout.read().decode())
    print("Error:", stderr.read().decode())

except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    cliente.close()
# Parar servidor 

# Iniciar Manejados

# Paar  Manajeados



