import socket
import time
client_name = input("Enter Client Name")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5000))

id = 0
client.send(client_name.encode())
server_name = client.recv(1024).decode()
try:
    while(1):
        msg = input(client_name + " : " + str(id) + " > ")
        client.send(f"{id} : {msg}".encode())
        data = client.recv(1024).decode()
        words = data.split(' ')
        id = int(data[0]) + 1
        print(server_name + " : " + data)
finally:       
    client.close()