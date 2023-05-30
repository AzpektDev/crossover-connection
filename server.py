import socket
from config import CONNECTION, read_data
from commands import commands

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

        print("received: " + data)

        command = data.split(" ")[0]
        if command in commands:
            response = commands[command]
        elif "list" in data:
            response = "pwd, ls, cd, nmap, netdiscover, rm, cp, mkdir, mv, dirb"
        else:
            response = "Command not found"

        conn.sendall(response.encode(FORMAT) + b"\r\n\r\n")

    conn.close()


if __name__ == "__main__":
    server_program()
