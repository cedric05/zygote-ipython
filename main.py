import os
import sys
import IPython
import argparse
from server import start_unix_socket_server

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--script", required=True,
	help="script file")
args = vars(ap.parse_args())

scriptfile = args['script']


# c = os.fork()
# if c == 0:
#     ## child
#     IPython.embed_kernel()
# else:
#     
start_unix_socket_server(scriptfile)
    ## parent