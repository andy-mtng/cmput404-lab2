import socket

BYTES_TO_READ = 4096


def get(host, port):
    request = b"GET / HTTP/1.\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Open socket
    s.connect((host, port))
    s.send(request)
    s.shutdown(socket.SHUT_WR)  # Complete sending
    result = s.recv(BYTES_TO_READ)  # Keep reading incoming data
    while (len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    s.close()  # Close the socket


# get("www.google.com", 80)
get("localhost", 8080)
