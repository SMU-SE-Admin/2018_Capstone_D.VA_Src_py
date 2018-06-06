import socket
import os, subprocess, thread

port = 5002
sock = socket.socket()
sock.bind(('',port))
print "create socket"

def openSendIp():
    subprocess.call("python "+os.path.join(os.getcwd(),"SendIp.py"))
thread.start_new_thread(openSendIp,())

while True:
    sock.listen(10)
    cli, info = sock.accept()
    print "cli accept"

    data = cli.recv(1024)
    cli.close()
    msg = data.split(":::")[0]
    print msg

    #os.system("python "+os.path.join(os.getcwd(),"StringClassify",msg))
    subprocess.call("python "+os.path.join(os.getcwd(),"StringClassify",msg))
