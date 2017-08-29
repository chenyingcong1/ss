#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket, time, psutil, os

def Connect():
    locakIP = socket.gethostbyname(socket.gethostname())
    remoteIP = '10.140.0.3'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    while 1:
        try:
            sock.connect((remoteIP, 4000))
            print('Connect server({}) success'.format(remoteIP))
            return sock
        except:
            print("Retry 4 sec later...")
            time.sleep(4)
def Client():
    while 1:
        try:
            sock = Connect()
            sock.send('register'.encode())
            recv = sock.recv(1024).decode()
            if 'success' in recv:
                while 1:
                    ent = input()
                    sock.send(ent.encode())
                    res = sock.recv(1024).decode()
                    print(type(res))
            sock.close()
        except ConnectionResetError as e:
            print(e)
            time.sleep(4)

if __name__ == '__main__':
    Client()