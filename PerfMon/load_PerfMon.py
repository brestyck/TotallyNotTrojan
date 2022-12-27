import socket
HOST = "192.168.1.202"
sock = socket.socket()
sock.connect((HOST, 9081))
sock.send("execpy".encode("utf-8"))
sock.send("")