import socket, sys, time, os, subprocess, signal

sock = socket.socket()
port = 5009
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',port))

path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)), "SearchObject", "SearchObject.py")
p = -1
print "done"
while True:
    sock.listen(10)
    cli, info = sock.accept()
    print "find cli accept"

    data = cli.recv(1024)
    msg = data.split(":::")[0]

    if msg == "now":
        p = subprocess.Popen(path.split(' '))
        print "now-----------send---------------"

    elif msg == "cancel":
        if p != -1:
            path = "kill -9 "+str(p.pid)
            p.send_signal(signal.SIGINT)
            subprocess.Popen(path.split(" "))
        cli.close()
        sock.close()
        print "find sock close"
        #sys.exit(0)
        break

    else :
        print "something wrong input-----------"

    cli.close()
