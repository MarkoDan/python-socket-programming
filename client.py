import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '192.168.8.120'
ADDR = (SERVER, PORT)

#Defines the socket for the client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#This function will send the message to the server.
def send(msg):
    #It grabs the passed message, it encodes it into utf-8 format, and is saves is into local variable
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    #It subtracts the length of the message with the HEADER.
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send('Hello World!')
input()
send('Hello World!')
input()
send('Hello World!')
input()
send('Hello World!')

send(DISCONNECT_MESSAGE)