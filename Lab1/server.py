import socket

server_name = input("Enter Server Name")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

conn, addr = server.accept()
print("Connected:", addr)
id = 0
try:
    data = conn.recv(1024)
    client_name = data.decode()
    conn.send(server_name.encode())
    while(1):
        data = conn.recv(1024).decode()
        words = data.split(' ')
        id = int(words[0]) + 1
        print(str(client_name)+ " : " + data)
        msg = input(str(server_name) + " : " + str(id) + " > ")
        conn.send(f"{id} : {msg}".encode())
finally:
    conn.close()
    server.close()