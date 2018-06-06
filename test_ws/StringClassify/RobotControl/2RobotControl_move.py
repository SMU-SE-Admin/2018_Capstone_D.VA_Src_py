import socket
sock = socket.socket()
sock.bind(('',5006))
sock.listen(10)
while True:
    cli, info = sock.accept()
    data = cli.recv(1024)
    data = data.split(":::")[0]
    print data
    
