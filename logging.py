import socket
import csv

# Logger for incoming connection data
def connection_logger():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 8000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Logger is running on %s:%s" % server_address)

    with open("/home/osboxes/Desktop/Honeypot/HoneyAccessLog.csv", "w", newline="") as log_file:
        log_writer = csv.writer(log_file)
        log_writer.writerow(["IP", "PORT", "TYPE"])

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print("Accepted connection from %s:%s" % client_address)
            
            # Log the incoming connection data
            log_writer.writerow([client_address[0], client_address[1], "TCP"])

            # Close the connection
            client_socket.close()

if __name__ == '__main__':
    connection_logger()
