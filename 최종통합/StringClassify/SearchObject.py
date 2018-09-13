import socket, base64, time

port = 5008
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',port))
print " create searchobject socket"

sock.listen(10)
cli, info = sock.accept()
print "search cli accept"

data = cli.recv(1024)
data = data.split(":::")[0]
print data

i = int(data)
recv_size = 1024
s = ""
while i>0 :
    if i>recv_size:
        s += cli.recv(recv_size)
    else:
        s += cli.recv(i)
    i -= recv_size
    time.sleep(0.005)
#print s

#img = base64.standard_b64decode(s)
f = open("test.png", "wb")
f.write(s)

print "recv end"

f.close()
cli.close()
sock.close()
