import argparse
import os
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
file = open('passwords.txt', 'r')
lines = file.readlines()
found = False
password_list = [line.strip() for line in lines]



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


def check(l):
    for i in list(itertools.product(*l)):
        message = "".join(i)
        request(message)
        if found:
            break
        #lib_list.append(lib)

for i in password_list:
    list_pass = []
    for j in i:
        list_pass.append([j, j.upper()])
    check(list_pass)
    if found:
        break


