import socket
import sys
import ssl

def save_data(connstream, data):
    f = open('<path_to_KEYDRIVE>/chunk.txt', 'w+')
    received = (data.decode('utf-8')).rstrip()
    with f:
        f.write(received)

def receive_data(connstream):
    data = connstream.read()
    while data:
        if not save_data(connstream, data):
            break
        data = connstream.read()

bindsocket = socket.socket()
bindsocket.bind(('', <client_port))
bindsocket.listen(5)
received = "empty"
f = open('<path_to_KEYDRIVE>/chunk.txt', 'w+')

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket, server_side = True, certfile = "../Files/ssl/recv_server.crt", keyfile = "../Files/ssl/recv_server.key")
    try:
        print('Receiving usb key chunk')
        receive_data(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
        f.close()
        print("Closed local file")
