import socket

# Create Server
SERVER, PORT = "127.0.0.1", 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Server
server.bind((SERVER, PORT))

# Connect to Host
server.listen()
client, address = server.accept()
print(f"Connection from {address} has been established!")

client.send(b"Connected to the server!")
client.close()
