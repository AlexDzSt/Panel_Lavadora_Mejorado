import socket

def process_message(message):
    if message == "Lavado Normal":
        return "Lavado estandar con agua tibia"
    elif message == "Ciclo Rapido":
        return "Lavado corto conagua fria"
    elif message == "Ropa de color":
        return "Recomendado paraproteger colores"
    elif message == "Ropa Blanca":
        return "Lavado caliente para eliminar   manchas"
    elif message == "Ciclo delicado":
        return "Lavado suave conagua fria"
    elif message == "Carga pesada":
        return "Lavado intenso  de agua caliente"
    else:
        return "Ciclo no reconocido"

def start_server():
    host = '172.30.5.14'  # Cambia esto a la IP de tu servidor
    port = 12345  # Escoge un puerto disponible

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Escucha una conexión entrante

    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            data = client_socket.recv(1024).decode()
            print(f"Received message: {data}")
            response = process_message(data)
            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error sending data: {e}")
        finally:
            client_socket.close()
            print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    start_server()
