import socket
import select

HEADER_LENGTH = 10

# Handles message receiving
def receive_msg(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False
    
if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    receive_msg(HOST, PORT)