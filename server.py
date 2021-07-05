import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

conn_dict = {"83.73.233.41" : "44455" }

while True: 
    message, address = server_socket.recvfrom(1024)
    message = message.decode("utf-8") 

    if message == "pulse":
        print("Heartbeat from: {}".format(address))
        conn_dict[address[0]] = address[1]
 
    else:

        print("{}:{} is requesting a connection to {}".format(address[0], address[1], message))

        #add the requester to the list 
        ipLookUp = message
     

        if ipLookUp in conn_dict.keys():
            server_socket.sendto(bytearray(conn_dict[ipLookUp], "utf8"), address)



            server_socket.sendto(bytearray())



            print("resolved it")
        else:
            server_socket.sendto(b'404', address)
            print("I could not resolve this")