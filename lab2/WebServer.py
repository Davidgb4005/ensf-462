import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(('0.0.0.0', 8080))
serverSocket.listen(1)

while True:
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()
    print('Connection Received')

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        f = open(filename[1:], "r")
        outputdata = f.read()
        f.close()

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(outputdata.encode('utf-8'))}\r\n"
            "Connection: close\r\n\r\n"
        )

        connectionSocket.sendall(response.encode())

        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError as e:
        print(e)

        body = "<html><body><h1>404 Error!</h1></body></html>"

        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(body.encode('utf-8'))}\r\n"
            "Connection: close\r\n\r\n"
            f"{body}"
        )

        connectionSocket.sendall(response.encode())

    finally:
        connectionSocket.close()