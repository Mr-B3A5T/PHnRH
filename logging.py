import socket
import csv

def packet_capture():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Packet capture server is running on %s:%s" % server_address)

    # Create a CSV file to store network access packet details
    with open("/home/osboxes/Desktop/Honeypot/HoneyAccessLog.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP Address", "Port", "Connection Type"])

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print("Accepted connection from %s:%s" % client_address)

            # Record network access packet details
            writer.writerow(list(client_address) + ["TCP"])

            # Close the connection
            client_socket.close()

if __name__ == '__main__':
    packet_capture()
