import os, thread, subprocess
import socket, sys, signal, time

path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),"RobotControl", "RobotControl_move.py")
#path = "python "+os.path.join(os.getcwd(),"StringClassify","RobotControl","RobotControl_move.py")
print path
print path.split(' ')
p1 = subprocess.Popen(path.split(' '))
print p1.pid


path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),"RobotControl", "Robot_frame.py")

#path = "python "+os.path.join(os.getcwd(),"StringClassify","RobotControl","Robot_frame.py")
print path
print path.split(' ')
p2 = subprocess.Popen(path.split(' '))
print p2.pid

path = "python "+os.path.join(os.path.dirname(os.path.abspath(__file__)),"RobotControl", "Find_object_name.py")
print path
print path.split(' ')
p3 = subprocess.Popen(path.split(' '))
print p3.pid

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',5007))
sock.listen(10)
while True:
    cli, info = sock.accept()
    data = cli.recv(1024)
    data = data.split(":::")[0]
    if data == "cancel":
        print data+"-------------------"
        path = "kill -9 "+str(p2.pid)
        print path
        subprocess.Popen(path.split(" "))
        time.sleep(1)

        path = "kill -9 "+str(p1.pid)
        print path
        subprocess.Popen(path.split(" "))
	time.sleep(1)

	path = "kill -9 "+str(p3.pid)
	print path
	subprocess.Popen(path.split(" "))
        time.sleep(2)
        print "all close--------------"

        cli.close()
        sock.close()
        break
