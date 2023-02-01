import socket
import cv2
import numpy as np
import csv

def loop_video(video_path):
    video = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video.read()

        if not ret:
            video = cv2.VideoCapture(video_path)
            continue

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

def cctv_honeypot_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("CCTV honeypot server is running on %s:%s" % server_address)

    video_path = 'fake_cctv_video.mp4'

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from %s:%s" % client_address)

        with open('network_data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['IP Address', 'Port', 'Connection Type', 'Packet Details'])
            writer.writerow([client_address[0], client_address[1], 'TCP', 'Packet details not recorded'])

        video = loop_video(video_path)
        client_socket.sendall(video)

        client_socket.close()

if __name__ == '__main__':
    cctv_honeypot_server()
