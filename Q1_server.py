import socket
import os
# import function to unpickle object
from pickle_file import unpickle_obj

def run_server(host, port, save_dir):
    """
    Receives a file from a client via socket connection and saves it to a specific directory
    
    Parameters:
    host: IP address of the server
    port: Port number that the server is listening on
    save_dir: Directory where the received file will be saved 
    
    Returns:
    None
    """
    try:
        # Ensure save_dir is a string
        save_dir = str(save_dir)

        # Check if save_dir is empty
        if not save_dir.strip():
            raise ValueError("Empty directory path provided.")

        # Convert the directory path to absolute path
        abs_save_dir = os.path.abspath(save_dir)

        # Create the directory if it doesn't exist
        os.makedirs(abs_save_dir, exist_ok=True)

        # Set up TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Bind socket to host port
            server_socket.bind((host, port))
            # Listen for an incoming connection
            server_socket.listen(1)
            print("Server is listening...")
            # Accept connection from client
            conn, addr = server_socket.accept()

            with conn:
                print(f"Connected by {addr}")
                # Receive pickled file data from client
                pickled_file_data = conn.recv(1024)
                # Unpickle file data
                file_data = unpickle_obj(pickled_file_data)

                # Save unpickled file data to specified directory
                file_path = os.path.join(abs_save_dir, 'received_file.txt')
                with open(file_path, 'wb') as file:
                    file.write(file_data)
                print(f"File saved to: {file_path}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    save_dir = input("Enter the directory to save the received file: ").strip()
    run_server(HOST, PORT, save_dir)

#To fix: {b''} Error occurred: [Errno 2] No such file or directory: b''
    
    # References
    # https://www.youtube.com/watch?v=D75-mUoUJC8&ab_channel=ParisNakitaKejser
    # https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
    # https://www.youtube.com/watch?v=D75-mUoUJC8&ab_channel=ParisNakitaKejser
    # https://pythonprogramming.net/pickle-objects-sockets-tutorial-python-3/
    # https://www.pythoncheatsheet.org/cheatsheet/file-directory-path