import socket
import csv
import time
import mimetypes

def get_mimetype(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def send_video(client_socket, filename):
    with open(filename, 'rb') as f:
        video = f.read()
        client_socket.sendall(b'HTTP/1.0 200 OK\r\n')
        client_socket.sendall(f'Content-Type: {get_mimetype(filename)}\r\n'.encode())
        client_socket.sendall(b'\r\n')
        client_socket.sendall(video)

def cctv_honeypot_server(video_filename):
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

        # Send the fake video
        send_video(client_socket, video_filename)

        # Log the connection information
        with open('/home/osboxes/Desktop/Honeypot/HoneyAccessLog.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), client_address[0], client_address[1]])

        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    cctv_honeypot_server('/home/osboxes/Downloads/cctv.mp4')
