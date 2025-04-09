import socket

# Create Server
SERVER, PORT = "127.0.0.1", 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Client
server.connect((SERVER, PORT))

msg = server.recv(1024).__str__()
print(msg)
