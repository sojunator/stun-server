import time
import socket

from threading import Thread
punched = False

def formatIpForUsage(address):
	# Assumes that string in the format looking like
	# "192.168.10.4:1234" is supplied

	result = address.split(":")

	if len(result) != 2:
		result[1] = int(result[1])
		return tuple(result)

	return f in chat

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
			sleep(1)
			data, address = sock.recvfrom(1024)
			print("I punched through to {} who said: {}".format(address[1], data.decode("utf-8")))
		except socket.timeout:
			print('REQUEST TIMED OUT')

def waitForPunch(sock):
	# What port is this?
	data = ""
	address = ""
	punchThroughTo  = ""
	while not punched:
		try:
			time.sleep(1)


			# expect a package from host corresponding to
			# "192.168.0.1:1234"
			data, address = sock.recvfrom(1024) 

			print("{} wants to talk to us".format(data.decode("utf-8")))
			punched = false
 
			punchThroughTo = formatIpForUsage(data)

		except socket.timeout:
			print('Waiting for a punch attempt')

	punched = false
	while not punched:
		try:
			time.sleep(1)
			sendto.socket(b'hi mark', punchThroughTo)
			data, address = socket.recvfrom(1024)
			
			print(data.decode("utf-8"))
		except socket.timeout:
			print('REQUEST TIMED OUT')

	print("We punched through")









client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)


request = b'83.73.233.41'
punchServerAddr = ("104.248.28.213", 12000)


mode = "punch"

t = Thread(target=holdPortOpenToSTUN, args=(punchServerAddr, client_socket))
t.start()

print("Talking to:{}".format(punchServerAddr[0]))

client_socket.sendto(request, punchServerAddr)
if mode == "punch":
	try:
		request = request.decode("utf-8")
		data, server = client_socket.recvfrom(1024)
		messageString = data.decode("utf-8")
 


		if messageString == "404":
			print("Host could not resolve this")
		else:
			punchThroughTo = formatIpForUsage(data)
			print("Host told me to contact via: {}:{}".format(request, messageString))
			punchThrough((request, punchThroughTo, client_socket))

	except socket.timeout:
		print('REQUEST TIMED OUT')
else:
	waitForPunch(client_socket)
