#!/usr/bin/env python
# sender.py

import sys
import socket
if __name__ == "__main__":
    if (len(sys.argv) < 2):
        port=3000
    else:
        port=sys.argv[2]
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname('0.0.0.0')
        s.bind((host, port))
        s.listen(1)

        conn,addr = s.accept()

        while(1):
            char = sys.stdin.read(1)
            sys.stdout.write(char)
            conn.send(char)
    except KeyboardInterrupt:
        conn.close()
