import argparse
import itertools
import socket
import string
from string import digits
from string import ascii_letters

parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("port")
args = parser.parse_args()
ip = args.ip
port = int(args.port)
client_socket = socket.socket()
address = (ip, port)
client_socket.connect(address)

lib = list(string.ascii_lowercase) + list(digits)
lib_list = [lib]
found = False

def request(message):
    global found
    data = message.encode()
    client_socket.send(data)
    response = client_socket.recv(1024)
    response = response.decode()
    if response == "Connection success!":
        print(message)
        found = True
        client_socket.close()
    return found


while not found:
    for i in list(itertools.product(*lib_list)):
        message = "".join(i)
        request(message)
        if found:
            break
    lib_list.append(lib)
