import socket
from config import CONNECTION, read_data
import os
import time

FORMAT = "utf-8"


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(CONNECTION)
    server_socket.listen(5)

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

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
            print (f"Received file from client: {file_name}.{file_type} ({file_size} bytes) - saved to recived/{file_name}-{ts}.{file_type}")
        else:
            print("Received from client: " + data)

        message = input("Enter your response: ")
        conn.sendall(message.encode(FORMAT) + b"\r\n\r\n")

        if message.lower().strip() == "bye":
            break

    conn.close()


if __name__ == "__main__":
    server_program()
