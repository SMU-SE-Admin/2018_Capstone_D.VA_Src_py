from socket import *
import socket as sk
import os, subprocess, thread

class recieve_broad:
    def __init__(self):
        self.s=socket(AF_INET, SOCK_DGRAM)
        self.s.bind(('',5000))

    def reci(self):
        print("may I??")
        m=self.s.recvfrom(1024)
        self.s.close()
        return m[1][0]

class send_my_ip:
    def __init__(self,ip):
        self.s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.robot_ip = ip
        self.port = 5001

    def send_ip(self):
        self.s.connect((self.robot_ip,self.port))
        my_ip = sk.gethostbyname(sk.gethostname())+":::"
        self.s.send(my_ip.encode())
        self.s.close()

if __name__=="__main__":
    while True:
        phone_ip = recieve_broad()
        ip = phone_ip.reci()
        print(ip)
        f = open(os.path.join(os.getcwd(),"StringClassify","RobotControl","ip.txt"),"w")
        f.write(ip)
        f.close()
        my_ip = send_my_ip(ip)
        my_ip.send_ip()
	
