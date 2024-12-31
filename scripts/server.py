import socket

def start():
    host = '127.0.0.1'
    port = 80
    # Server side socket jazz -> create, bind, listen and accept followed by receive and send
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((host, port))
    s_socket.listen(4)
    c_socket, c_address = s_socket.accept()
    
    while True:
        data = c_socket.recv(1024)
        print(data.decode())
    c_socket.close()
    
if __name__ == "__main__":
    start()