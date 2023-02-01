import socket
import csv

def cctv_honeypot_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("CCTV honeypot server is running on %s:%s" % server_address)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from %s:%s" % client_address)

        with open('network_data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(client_address)

        client_socket.close()

if __name__ == '__main__':
    cctv_honeypot_server()
