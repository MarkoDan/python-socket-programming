import socket
import threading

HEADER = 64
PORT = 5050
#It gets the IP address of the computer by name
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# Define the socket that is going to allow us to communicate to other devices, is accepts IPV4 and streaming data through the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#The binding allows us to associate the socket with anything that connects to the address(ADDR)
server.bind(ADDR)

def handle_client(conn, addr):
    #It prints the IP address of who connected to the server.
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        #It accepts the message from the client if max size of 64 bytes and decodes it into utf-8 format.
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length is not None:
            #It converts it into int, and it defines the size of the actual message.
            message_length = int(message_length)
            message = conn.recv(message_length).decode(FORMAT)
            #It disconnects the connection if the message is Disconnect_message.
            if message == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr} {message}]')
            conn.send('Message received'.encode(FORMAT))
    conn.close()
#Allows the server to listen to connection and pass them to the handle_client() function. It distribute the connections.
def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        #IT waits for the connection, once connection has been achieved, it stores it to conn, and addr variables
        conn, addr = server.accept()
        # When the new connection has been established, it passes to the handle_client function with the args of conn and addr
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #It prints all the active connection
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


#It starts the server
print('[STARTING] server is starting...')
start()