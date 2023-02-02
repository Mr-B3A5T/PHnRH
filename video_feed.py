import socket
import cv2

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

    # Open the video file
    video = cv2.VideoCapture("/home/osboxes/Downloads/cctv.mp4")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from %s:%s" % client_address)

        # Send a fake CCTV video stream
        while True:
            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            client_socket.sendall(jpeg.tobytes())

        # Close the connection
        client_socket.close()
        video.release()

if __name__ == '__main__':
    cctv_honeypot_server()
