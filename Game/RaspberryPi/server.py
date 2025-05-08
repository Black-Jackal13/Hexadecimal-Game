import socket

# Create Server
SERVER, PORT = "127.0.0.1", 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Server
server.bind((SERVER, PORT))

# Connect to Host
server.listen()
print(f"Server is listening on {SERVER}:{PORT}...")
client, address = server.accept()
print(f"Connection from {address} has been established!")

client.send(b"EB00010001")
client.close()
server.close()
