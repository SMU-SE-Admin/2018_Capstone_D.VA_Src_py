import socket, sys, os

port = 5003
sock = socket.socket()
sock.bind(('',port))
print "create login socket"

sock.listen(10)
cli, info = sock.accept()
print "login cli accept"

data = cli.recv(1024)
f = open(os.path.join(os.getcwd(),"StringClassify","logininfo.txt"),"r")
loginlist = {}
while True:
    line = f.readline()
    if not line: break
    line = line[:-1]
    line = line.split('\t')
    loginlist[line[0]] = line[1]
f.close()

data = data.split(":::")
for key, value in loginlist.items():
    if key == data[0] and value == data[1]:
        print "login accept"
        cli.send("yes:::")
        cli.close()
        sock.close()
        sys.exit(0)

print "fail to login"
cli.send("no:::")
cli.close()
sock.close()




