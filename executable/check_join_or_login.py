from socket import *
import os
import platform
class recieve_id_pass:
    def __init__(self):
        self.s=socket(AF_INET,SOCK_STREAM)
        self.s.bind(("",12223))

    def re_id_ps(self):
        self.s.listen(10)
        self.conn, addr = self.s.accept()
        data = self.conn.recv(1024)
        id_pass = data.decode()
        return id_pass
#        id_pass_list = id_pass.split(':::')
#        if len(id_pass_list) == 2:
#            user_id = id_pass_list[0]
#            user_pass = id_pass_list[1]
#            self.check_id_pass(user_id, user_pass, conn)
#        else:
#            user_id = id_pass_list[0]
#            user_pass = id_pass_list[1]
#            user_sn = id_pass_list[2]
#            pass
#        return user_id, user_pass, conn
    
    def check_id_pass(self, info):
        self.conn.send(info.encode())

class sign(object):
    THISFOLDER = os.path.dirname(os.path.abspath(__file__))
    def signin(self, memid, mempw):
        f = open(os.path.join(self.THISFOLDER,"memberlist.txt"), 'r')
        while True:
            line = f.readline()
            if not line:
                break
            line = line[:-1]
            line = line.split('\t')
            print(line)
            if (line[0] == memid) and (line[1] == mempw):
                f.close()
                return "yes:::"
            else:
                f.close()
                return "no:::"
        return "no:::"
    def signup(self, memid, mempw):
        f = open(os.path.join(self.THISFOLDER,"memberlist.txt"), 'a')
        info = memid+'\t'+mempw+'\n'
        f.write(info)
        f.close()
        return "yes:::"
    def valid_sn(self, sn):
        f = open(os.path.join(self.THISFOLDER,"sn.txt"), 'r')
        serial = f.readline()
#	serial = serial[:-1]
        print(serial)
        f.close()
        if serial == sn:
                return True
        else:
                return False
    def split_string(self, info):	
        info = info.split(':::')
        if len(info) == 2:
            return self.signin(info[0], info[1])
        else:
            if self.valid_sn(info[2]):
                return self.signup(info[0], info[1])
            return "no:::"

if __name__=="__main__":
    id_pass = recieve_id_pass()
    while True:
        check_id = id_pass.re_id_ps()
        checking = sign()
        info = checking.split_string(check_id)
        print(info)
        id_pass.check_id_pass(info)
