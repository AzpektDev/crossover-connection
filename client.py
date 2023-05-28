import socket
from config import CONNECTION, read_data
import os
from utils.utils import cls
import time
from colorama import Fore, Style

cls()

def client_program():
    client_socket = socket.socket()
    client_socket.connect(CONNECTION)

    while True:
        message = input("Enter your message: ")

        message_is_file = False
        try:
            with open(message, 'r') as f:
                message_is_file = True
        except FileNotFoundError:
            pass

        if message_is_file:
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

        is_file = False
        
        if data.startswith("FILE-"):
            is_file = True

            ts = time.time()


            file_header = data.split('\r\n')[0]
            file_type = file_header.split('-')[1]
            file_size = int(file_header.split('-')[2])
            file_name = file_header.split('-')[3]
            file_contents = data.split('\r\n')[1]
            
            if not os.path.exists('recived'):
                os.mkdir('recived')

            with open(f"recived/{file_name}-{ts}.{file_type}", 'w') as f:
                f.write(file_contents)

        if is_file:
            print(f"{Fore.LIGHTWHITE_EX}Received file from client: {file_name}.{file_type} ({file_size} bytes) - saved to recived/{file_name}-{ts}.{file_type}{Style.RESET_ALL}")
        else:
            print("Received from client: " + data)

    client_socket.close()

if __name__ == '__main__':
    client_program()
