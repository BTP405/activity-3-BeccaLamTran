import socket
import os
 # Importing pickle_obj function from pickle_file
from pickle_file import pickle_obj 


def run_client(host, port, file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return
    
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        # Pickle and send file data
        pickle_obj(file_data, file_path)  # Pass both file_data and file_path to pickle_obj

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    file_path = input("Enter the file path to transfer: ")
    run_client(HOST, PORT, file_path)
