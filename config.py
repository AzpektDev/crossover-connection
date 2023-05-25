IP = '192.168.1.3'
PORT = 65433
CONNECTION = (IP, PORT)

def read_data(socket):
    data = b''
    while b'\r\n\r\n' not in data:
        data += socket.recv(1)
    return data