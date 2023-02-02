import socket
import csv

# Create a fake CCTV server
def cctv_honeypot_server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("CCTV honeypot server is running on %s:%s" % server_address)

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from %s:%s" % client_address)
        
        # Log the connection details
        with open('/home/osboxes/Desktop/Honeypot/HoneyAccessLog.csv', 'a') as logfile:
            writer = csv.writer(logfile)
            writer.writerow([client_address[0], client_address[1], 'TCP'])

        # Read the video from the local directory
        with open('/home/osboxes/Downloads/cctv.mp4', 'rb') as video_file:
            video_stream = video_file.read()

        # Send the video stream
        client_socket.sendall(video_stream)

        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    cctv_honeypot_server()
