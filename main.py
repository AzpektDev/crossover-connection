import os
import time
import signal
import socket
from config import CONNECTION, IP, PORT, read_data

print("-----------------------------------")
print("        choose client/server       ") 
print("-----------------------------------")
print("created by AzpektDev & Al33ks")
print("\t\"s\" --- server")
print("\t\"c\" --- client")
print("To quit press \"q\"") 

choice = input()

if choice == 's':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(CONNECTION)
        print(f'Server binded to {IP}:{PORT}')
        s.listen(5)

        while True:
          client, addr = s.accept()
          print(f"Connected to {addr[0]}:{addr[1]}")

          data = b''
          while b'\r\n\r\n' not in data:
              data += client.recv(1024)

          data = data.decode()
          data = data.split('\r\n\r\n')
          data = data[0]
          
          print(data)

          client.close()

elif choice == 'c':
    print(f"Starting client at {CONNECTION}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect(CONNECTION)
        data = input("Data to send: ")
        request = f"{data}\r\n\r\n"
        server.sendall(request.encode())

        response = read_data(server).decode()
elif choice == 'q':
    SystemExit("Quitting program") 
else:
    for x in range(100):
        print("Skill issue lmao Bro cant even type a letter")
    time.sleep(1)
    os.kill(os.getppid(), signal.SIGHUP)
