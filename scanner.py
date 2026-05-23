import socket

target = "127.0.0.1" #ma machine
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
result = s.connect_ex((target, port))

if result == 0:
    print("Port " + str(port) + " is open")
else:
    print("Port " + str(port) + " is not open")