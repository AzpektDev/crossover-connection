import socket
from config import CONNECTION, read_data

def client_program():
    client_socket = socket.socket()
    client_socket.connect(CONNECTION)

    while True:
        message = input("Enter your message: ")
        client_socket.sendall(message.encode() + b"\r\n\r\n")

        if message.lower().strip() == 'bye':
            break

        data = read_data(client_socket).decode().strip()
        print("Received from server: " + data)

    client_socket.close()

if __name__ == '__main__':
    client_program()
