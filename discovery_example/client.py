import zmq
from discovery_pb2 import DiscoveryReq, DiscoveryResp

context = zmq.Context()

print("Connecting....")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(10):
	req = DiscoveryReq()
	req.msg_type = 2
	print(f"Sending request {request} ...")
	socket.send_string(req.SerializeToString().decode())

	message = DiscoveryResp.FromString(socket.recv())
	print(f"Received reply {request} [ {message} ]")
