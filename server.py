import socket
from config import CONNECTION, read_data
import os
import time
from utils.utils import cls, center_text
from colorama import Fore, Style

FORMAT = "utf-8"

cls()

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(CONNECTION)
    server_socket.listen(5)

    print(f"{Fore.GREEN}Server is running!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Awaiting connection...{Style.RESET_ALL}")

    conn, address = server_socket.accept()
    print(f"{Fore.BLUE}Connection from: {str(address)}{Style.RESET_ALL}")

    while True:
        data = read_data(conn).decode().strip()
        if not data:
            break

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
            print (f"{Fore.LIGHTWHITE_EX}Received file from client: {file_name}.{file_type} ({file_size} bytes) - saved to recived/{file_name}-{ts}.{file_type}{Style.RESET_ALL}")
        else:
            print("Received from client: " + data)

        message = input("Enter your response: ")

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

        conn.sendall(message.encode(FORMAT) + b"\r\n\r\n")

        if message.lower().strip() == "bye":
            break

    conn.close()


if __name__ == "__main__":
    server_program()
