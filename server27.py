#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket, time, os
def Server():
    locakIP = socket.gethostbyname(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((locakIP,4000))
    sock.listen(10)
    print"server start"
    # sock.settimeout(8)
    while 1:
        try:
            connection, address = sock.accept()
            while 1:
                data = connection.recv(1024).decode()
                if not data:
                    break
                elif data == 'register':
                    print'Client:'+address[0]+' connect success'
                    connection.send("register success".encode())
                elif data == 'ip':
                    connection.send(address[0].encode())
                elif data == 'account':
                    account = os.system('/root/ss-bash/ssadmin.sh showpw')
                    connection.send(account.encode())
                else:
                    connection.send(data.encode())
            connection.close()
        except Exception as e:
            print Exception, ':', e
            time.sleep(4)
if __name__ == '__main__':
    Server()