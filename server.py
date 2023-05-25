import socket
from config import CONNECTION

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(CONNECTION)
    s.listen(5)

    while True:
      client, addr = s.accept()
      print(f"Connected to {addr[0]}:{addr[1]}")

      data = b''
      while b'\r\n\r\n' not in data:
          data += client.recv(1024)

      data = data.decode()

      print(data)

      client.close()

        