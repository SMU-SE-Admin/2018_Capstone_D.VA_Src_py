import socket, sys, os, time

port = 5004
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',port))
print "create signup socket"

sock.listen(10)
cli, info = sock.accept()
print "signup cli accept"

data = cli.recv(1024)

print "get data"

#read login list
pro = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logininfo.txt")
print pro

#f = open(os.path.join(os.getcwd(), "StringClassify", "logininfo.txt"), "r")
f = open(pro, "r")
loginlist = {}
while True:
    line = f.readline()
    if not line: break
    line = line[:-1]
    line = line.split('\t')
    loginlist[line[0]] = line[1]
f.close()

data = data.split(":::")
#if id exist then fail
if data[0] in loginlist:
    print "noid:::"
    cli.send("noid:::")
    cli.close()
    sock.close()
    print "sock close"
    sys.exit(0)

#if wrong serial number
#f1 = open(os.path.join(os.getcwd(), "StringClassify", "serialnumber.txt"), "r")
pro2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),"serialnumber.txt")
print pro2

f1 = open(pro2, "r")
serialnum = f1.readline()
print serialnum
f1.close()
if data[2] != serialnum:
    print data[2]+", "+serialnum
    cli.send("noserial:::")
    cli.close()
    sock.close()
    sys.exit(0)

#accept signup
cli.send("yes:::")
#f2 = open(os.path.join(os.getcwd(), "StringClassify", "logininfo.txt"), "w")
f2 = open(pro, "w")
loginlist[data[0]] = data[1]
for key, value in loginlist.items():
    f2.write(key+'\t'+value+'\n')
f2.close()
cli.close()
sock.close()
