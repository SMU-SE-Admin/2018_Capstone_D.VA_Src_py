import socket, subprocess, os, signal, time
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',5006))
sock.listen(10)

data2 = "RobotControl_base_stop.py"
path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),"RobotConrtrol_move_base",data2)
p = subprocess.Popen(path.split(' '))

while True:
    cli, info = sock.accept()
    data1 = cli.recv(1024)
    data1 = data1.split(":::")[0]
    print data1
    if data1 == "cancel":
        path = "kill -9 "+str(p.pid)
        p.send_signal(signal.SIGINT)
        subprocess.Popen(path.split(" "))
        path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),"RobotConrtrol_move_base","RobotControl_base_stop.py")
        p = subprocess.Popen(path.split(' '))
        time.sleep(1)
        path = "kill -9 "+str(p.pid)
        p.send_signal(signal.SIGINT)
        subprocess.Popen(path.split(" "))
        print "sock close"
        cli.close()
        sock.close()
        break

    if data2 != data1:
        path = "kill -9 "+str(p.pid)
        p.send_signal(signal.SIGINT)
        subprocess.Popen(path.split(" "))
        path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),"RobotConrtrol_move_base",data1)
        p = subprocess.Popen(path.split(' '))
        data2 = data1
    
