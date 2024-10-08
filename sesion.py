from logging import root
import paramiko
import time

from getpass import getpass

host = "10.250.8.106"

usuario: "root"

if __name__ == '__main__':
    try:
        cliente= paramiko.SSHClient()
        clave = getpass("clave: ")
        cliente.connect(host, username=usuario, password=clave)
        
        
        stand_input, stand_output, stand_error= cliente.exec_command("ls /")
        time.sleep(1)
        
        resultado = stand_output.read().decode()
        print(resultado)
        
        cliente.close()
        
    except paramiko.ssh_exeption.AuthenticationExeption as e:
        print("No se pudo conectar")
        
        
        