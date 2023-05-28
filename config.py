ip = "localhost"
port = 8080
CONNECTION = (ip, port)


def read_data(socket):
    data = b""
    while b"\r\n\r\n" not in data:
        data += socket.recv(1)
    return data
