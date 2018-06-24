import socket

sock = socket.socket()
port = 5009
sock.bind(('',port))

print "done"
while True:
    sock.listen(10)
    cli, info = sock.accept()

    cli.send("testing:::")
    cli.close()
