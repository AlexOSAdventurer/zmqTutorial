import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting ...")
socket.connect("tcp://localhost:5556")

socket.setsockopt_string(zmq.SUBSCRIBE, "10001")

for update_nbr in range(5):
	string = socket.recv_string()
	zipcode, temperature, relhumidity = string.split()
	print(zipcode, temperature, relhumidity)

