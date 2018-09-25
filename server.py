import socket
import sys
import os
import IPython
import signal
import importlib

def execute_script(scriptfile):
    return importlib.import_module(scriptfile)




def create_process(locals):
    c = os.fork()
    if c ==0:
        IPython.embed_kernel(locals)
    else:
        return c


def start_unix_socket_server(scriptfile):
    server_address = './uds_socket'
    # Make sure the socket does not already exist
    try:
        os.unlink(server_address)
    except OSError:
        if os.path.exists(server_address):
            raise
    locals = execute_script(scriptfile)
    child_process_id = create_process(locals)
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Bind the socket to the port
    print('starting up on %s' % server_address)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            pass
            os.kill(child_process_id, signal.SIGKILL)
            c = create_process(locals)
            # print('connection from', client_address)
            # # Receive the data in small chunks and retransmit it
            # while True:
            #     data = connection.recv(16)
            #     print('received "%s"' % data)
            #     if data:
            #         print('sending data back to the client')
            #         # connection.sendall(data)
            #     else:
            #         print('no more data from', client_address)
            #         break
        finally:
            print('connection closed')
            # Clean up the connection
            connection.close()

# if __name__=='__main__':
#     start_unix_socket_server()