from socket import *
import socket as sk

class recieve_broad:
    def __init__(self):
        self.s=socket(AF_INET, SOCK_DGRAM)
        self.s.bind(('',50000))

    def reci(self):
        print("may I??")
        m=self.s.recvfrom(1024)
        self.s.close()
        return m[1][0]

class send_my_ip:
    def __init__(self,ip):
        self.s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.robot_ip = ip
        self.port = 12222

    def send_ip(self):
        self.s.connect((self.robot_ip,self.port))
        my_ip = sk.gethostbyname(sk.gethostname())+":::"
        self.s.send(my_ip.encode())
        self.s.close()

class recieve_id_pass:
    def __init__(self):
        self.s=socket(AF_INET,SOCK_STREAM)
        self.s.bind(("",12223))

    def re_id_ps(self):
        self.s.listen(10)
        conn, addr = self.s.accept()
        data = conn.recv(1024)
        id_pass = data.decode()
        id_pass_list = id_pass.split(':::')
        if len(id_pass_list) == 2:
            user_id = id_pass_list[0]
            user_pass = id_pass_list[1]
            self.check_id_pass(user_id, user_pass, conn)
        else:
            user_id = id_pass_list[0]
            user_pass = id_pass_list[1]
            user_sn = id_pass_list[2]
            pass
        return user_id, user_pass, conn
    
    def check_id_pass(self, user, user_pass, conn):
        print("id : "+user)
        print("pass : "+user_pass)
        count = 0
        if user == "test_id":
            count +=1
        if user_pass == "test_pass":
            count +=1
        if count == 2:
            conn.send("yes".encode())
        else :
            conn.send("no".encode())
        
        
if __name__=="__main__":
    #while True:
    #    phone_ip = recieve_broad()
    #    ip = phone_ip.reci()
    #    print (ip)
    #    my_ip = send_my_ip(ip)
    #    my_ip.send_ip()
    phone_ip = recieve_broad()
    ip = phone_ip.reci()
    print (ip)
    my_ip = send_my_ip(ip)
    my_ip.send_ip()
    id_pass = recieve_id_pass()  
    id_pass.re_id_ps()
        
