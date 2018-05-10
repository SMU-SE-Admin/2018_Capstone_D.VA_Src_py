import socket
import threading
import rospy
from geometry_msgs.msg import Twist


class GoForward():
    def __init__(self):
        # initiliaze
        rospy.init_node('GoForward', anonymous=False)

        # tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c
        rospy.on_shutdown(self.shutdown)

        # Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
        self.cmd_vel = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)

        # TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        self.r = rospy.Rate(10);

        # Twist is a datatype for velocity
        self.move_cmd = Twist()

    def pub(self,a):
        if a == "go_forward":
            self.move_cmd.linear.x = 0.1
            self.move_cmd.angular.z = 0
        elif a == "turn_right":
            self.move_cmd.linear.x = 0
            self.move_cmd.angular.z = -0.5
        elif a == "turn__left":
            self.move_cmd.linear.x = 0
            self.move_cmd.angular.z = 0.5
        elif a =="move__back":
            self.move_cmd.linear.x = -0.1
            self.move_cmd.angular.z = 0
        else:
            self.move_cmd.linear.x = 0
            self.move_cmd.angular.z = 0
        # let's go forward at 0.2 m/s
#        move_cmd.linear.x = 0.2
        # let's turn at 0 radians/s
#        move_cmd.angular.z = 0

        self.cmd_vel.publish(self.move_cmd)

        # as long as you haven't ctrl + c keeping doing...
        #while not rospy.is_shutdown():
            # publish the velocity
         #   self.cmd_vel.publish(move_cmd)
            # wait for 0.1 seconds (10 HZ) and publish again
          #  r.sleep()

    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
        # a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
        # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)

class Recv_string:
    msg = ""

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('', 12225))
#        print('init end')

    def connect_and_recv(self):
        self.sock.listen(10)
#        print('wait client')
        cli, info = self.sock.accept()
#        print('client accepted')
        msg = self.recv_string(cli)
        return msg

    def recv_string(self, cli):
        data = cli.recv(1024)
        cli.close()
        msg = data.split(":::")[0]
        return msg

    def run(self):
        go = GoForward()
        while (True):
            msg = self.connect_and_recv()
            print(msg)
            go.pub(msg)

    def get_msg(self):
        return self.msg

if __name__=='__main__':
	recv = Recv_string()
	t = threading.Thread(target = recv.run())
	t.start()
