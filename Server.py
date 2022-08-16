import socket

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

# number of requests should listen = 1 parameter
sock.listen(1)
print("the server is running and is listening to client request")

# return connection and address of client
connection, address = sock.accept()

message = "Hey there is something important for you"
connection.send(message.encode())

connection.close()
