import socket
from config import CONNECTION, read_data

print(f"starting client at {CONNECTION}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect(CONNECTION)
    name = input("What's your name:")
    request = f"HELLO\r\n{name}\r\n\r\n"
    server.sendall(request.encode())

    response = read_data(server).decode()
