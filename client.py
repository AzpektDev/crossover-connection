import socket
from config import CONNECTION, read_data
import os
from utils.utils import cls

cls()

def client_program():
    client_socket = socket.socket()
    client_socket.connect(CONNECTION)

    while True:
        message = input("Enter your message: ")

        is_file = False
        try:
            with open(message, 'r') as f:
                is_file = True
        except FileNotFoundError:
            pass

        if is_file:
            file_type = message.split('.')[-1]
            file_size = os.path.getsize(message)
            file_name = os.path.basename(message)
            file_name = file_name.split('.')[0]

            with open(message, 'r') as f:
                file_contents = f.read()

            message = f"FILE-{file_type}-{file_size}-{file_name}\r\n{file_contents}\r\n\r\n"

        client_socket.sendall(message.encode() + b"\r\n\r\n")

        if message.lower().strip() == 'bye':
            break

        data = read_data(client_socket).decode().strip()
        print("Received from server: " + data)

    client_socket.close()

if __name__ == '__main__':
    client_program()
