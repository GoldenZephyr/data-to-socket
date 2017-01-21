#!/usr/bin/env python

import socket
import sys

if __name__=="__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host=sys.argv[1]
        port=int(sys.argv[2])
        s.connect((host,port))

        while(1):
            char = s.recv(1)
            sys.stdout.write(char)
    except KeyboardInterrupt:
        s.close()
