import socket
import sys


#create socket ie connect 2 comps
def socket_create():
    try:
        global host #ip add of host
        global port 
        global s
        host = ''
        port = 9999
        s=socket.socket() 
    except socket.error as msg:
        print('Socket creation error: ' + str(msg))

#bind soc to the port and wait for connection hehe
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host,port)) #host is usually ip add but since its our local chilling
        s.listen(5)#allows server to accept connections where 5 is no of bad connc b4 refusing
    except socket.error as msg:
        print("socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind




