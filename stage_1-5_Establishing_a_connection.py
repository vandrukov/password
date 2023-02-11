import argparse
import socket


parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("port")
parser.add_argument("message")
args = parser.parse_args()
ip = args.ip
port = int(args.port)
message = args.message


client_socket = socket.socket()
address = (ip, port)
client_socket.connect(address)
data = message.encode()
client_socket.send(data)
response = client_socket.recv(1024)
response = response.decode()
print(response)
client_socket.close()
