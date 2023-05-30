import socket
from config import CONNECTION, read_data

FORMAT = "utf-8"


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(CONNECTION)
    server_socket.listen(5)

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = read_data(conn).decode().strip()
        if data:
            break
        print("Received from client: " + data)

        message = input("Enter your response: ")
        conn.sendall(message.encode(FORMAT) + b"\r\n\r\n")

        if message.lower().strip() == "bye":
            break

    conn.close()


if __name__ == "__main__":
    server_program()
