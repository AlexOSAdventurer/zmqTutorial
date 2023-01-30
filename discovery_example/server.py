import time
import zmq
from discovery_pb2 import DiscoveryReq, DiscoveryResp

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
poller = zmq.Poller()

poller.register(socket, zmq.POLLIN)

while True:
	events = dict(poller.poll())
	if socket in events:
		message = DiscoveryReq.FromString(socket.recv())
		print(f"Received request: {message}")

		time.sleep(1)
		resp = DiscoveryResp()
		resp.msg_type = 2
		resp.is_ready.reply = True
		socket.send_string(resp.SerializeToString().decode())
	else:
		print("No event!")
		time.sleep(0.1)

