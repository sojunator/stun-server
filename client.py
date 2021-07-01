import time
import socket

from threading import Thread
punched = False
def holdPortOpenToSTUN(addr, socket): 
    while not punched:
        socket.sendto(b'pulse', addr)
        print("maintaining the port open")

        time.sleep(5)

def punchThrough(address, sock):  
    print("attempting to punch through to: {}".format(address)) 

    while not punched:
        sock.sendto(b'hi mark', address)
        try:
            sock.recvfrom(1024) 
        except socket.timeout:
            print('REQUEST TIMED OUT')

 



client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
request = b'89.233.217.40'
addr = ("104.248.28.213", 12000)
mode = "punch"

t = Thread(target=holdPortOpenToSTUN, args=(addr, client_socket))
t.start()

print("Talking to:{}".format(addr[0]))

client_socket.sendto(request, addr)
if mode == "punch":
    try:
        request = request.decode("utf-8")
        data, server = client_socket.recvfrom(1024)
        messageString = data.decode("utf-8")

        if messageString == "404":
            print("Host could not resolve this")
        else:
            print("Host told me to contact via: {}:{}".format(request, messageString))
            punchThrough((request, int(messageString)), client_socket)
    except socket.timeout:
        print('REQUEST TIMED OUT')

