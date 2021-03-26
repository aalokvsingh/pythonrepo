import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 1234  # socket server port number

    client_socket = socket.socket()  # Create a socket object 
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive data stream. it won't accept data packet greater than 1024 bytes
        print('Data Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()




