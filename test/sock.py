from socket import *
from threading import Thread
import os
import sys
import time

class Sock(object):
        def create_serv(self, PORT):
                HOST = 'localhost'
                #PORT = 12224
                ADDR = (HOST,PORT)
                BUFSIZE = 4096

                serv1 = socket(AF_INET, SOCK_STREAM)

                #filename = "C:\\i.png"

                #Bind Socket
                serv1.bind(ADDR)
                serv1.listen(0)
                conn, addr1 = serv1.accept()

                sock = (serv1, conn)

                return sock
#       print('client connected ... ', addr)

        def send_image(self, conn, filename):
                THISFOLDER = os.path.dirname(os.path.abspath(__file__))
                #Open the file

                #Read and then Send to Client
                f=open(os.path.join(THISFOLDER,filename),'rb')# open file as binary
                data=f.read()
        #       print (data,',,,')
                exx=conn.send(str(len(data)).encode())
                print(len(data))
                print(type(data))
                print(type(data[0]))
                exx=conn.sendall(data)
        #       print (exx,'...')
                f.flush()
                f.close()
        #Close the Socket 
#       print ('finished writing file')
        def disconnect(self, sonn, serv):
                conn.close()
                serv.close()

        def create_client(self, PORT):
                HOST = 'localhost'
                client = socket(AF_INET, SOCK_STREAM)
                ADDR = (HOST, PORT)

                client.connect(ADDR)

                return client

sock = Sock()
ser = sock.create_serv(12224)
#while True:
sock.send_image(ser[1],"test6.jpg")
#        time.sleep(1)
#ser2 = sock.create_serv(12225)
#while(True):
#       ser[1].send(b'Hi')
#       ser2[1].send(b'hello')



