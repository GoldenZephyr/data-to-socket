#!/usr/bin/env python
import sys
import socket
if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host="localhost"
        port=3001
        s.bind((host, port))
        s.listen(1)

        conn,addr = s.accept()

        while(1):
            char = sys.stdin.read(1)
            sys.stdout.write(char)
            conn.send(char)
    except KeyboardInterrupt:
        conn.close()
