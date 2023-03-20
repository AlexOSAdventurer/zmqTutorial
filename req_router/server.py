import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://*:5555")

while True:
	if (socket.poll(timeout=10) == zmq.POLLIN):
		address, empty, byte_msg = socket.recv_multipart()
		print(f"Received request: {byte_msg}")

		time.sleep(1)

		socket.send_multipart([
			address,
			b'',
			b'World'
		])

