#!/usr/bin/env python
# coding:utf-8

import socket

from handler import handle_connection

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)

try:
    while True:
        conn, address = serversocket.accept()
        handle_connection(conn, address)
finally:
    serversocket.close()
