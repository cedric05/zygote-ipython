import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sock.connect('uds_socket')
sock.send('reload')
sock.close()