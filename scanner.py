import socket

target = "127.0.0.1" #ma machine
port = 22

def port_scan(target, port, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((target, port))
    s.close()
    return result==0



target = "127.0.0.1" #ma machine
for port in range(1, 1025):
    if port_scan(target, port):
        print("Port " + str(port) + " is open")

print("Scan completed")