# first of all import the socket library
import socket


def server_program():
    #create a socket object name it server_socket
    server_socket = socket.socket()
    print ("Socket successfully created")

    # get the hostname
    host = socket.gethostname()
    port = 1234  # reserver any port in your computer, initiate port no above 1024

    # The bind() function takes hostname and port as argument
    server_socket.bind((host, port))  # bind host address and port together
    print ("socket binded to ip %s port %s" %(host,port))

    # put socket into listning mode and configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print ("socket is listening")  
    
    conn, address = server_socket.accept()  # make connection with client and accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("data from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()