import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

conn_dict = {"83.73.233.41" : "44455" }

while True:
    try: 
        message, address = server_socket.recvfrom(1024)
        message = message.decode("utf-8") 
        conn_dict[address[0]] = address[1]

        if message == "pulse":
            print("Heartbeat from: {}".format(address)) 
     
        else:

            print("{}:{} is requesting a connection to {}".format(address[0], address[1], message))
 
            ipLookUp = message
         

            if ipLookUp in conn_dict.keys():
                server_socket.sendto(bytearray(conn_dict[ipLookUp], "utf-8"), address)
                
                puncherAddress = list(address)
                puncherAddress[1] = str(puncherAddress[1])
                puncherAddress = ":".join(puncherAddress)




                puncheAddress = (ipLookUp, int(conn_dict[ipLookUp]))

                print("Telling {} that {} wants to punch them.".format(puncheAddress, puncherAddress))
                server_socket.sendto(bytearray(puncherAddress, "utf-8"), puncheAddress)



                print("resolved it")
            else:
                server_socket.sendto(b'404', address)
                print("I could not resolve this")
    except:
        print("Waiting for connection") 