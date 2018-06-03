import socket
import os

sock = socket.socket()
sock.bind(('',5001))
print "create socket"

while True:
    sock.listen(10)
    cli, info = sock.accept()
    print "cli accept"

    data = cli.recv(1024)
    cli.close()
    msg = data.split(":::")[0]
    print msg

    os.system("python "+os.path.join(os.getcwd(),msg))