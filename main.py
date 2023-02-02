import socket

def video_server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Video server is running on %s:%s" % server_address)

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from %s:%s" % client_address)

        # Send a fake video stream
        with open("/home/osboxes/Downloads/cctv.mp4", "rb") as f:
            video_stream = f.read()
            client_socket.sendall(video_stream)

        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    video_server()
