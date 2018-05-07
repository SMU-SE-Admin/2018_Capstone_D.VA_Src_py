import rospy
from geometry_msgs.msg import Twist

class Move():
	self.direction = 0
	def __init__(self,direct):
		rospy.init_node('Move', anonymous = False)
		rospy.on_shutdown(self.shutdown)
		self.cmd_vel = rospy.Publisher('topic',Twist, queue_size=10)
		move_cmd = Twist()
		self.direction = direct
		if self.direction == 1:
			move_cmd.linear.x = 0.2
			move_cmd.angular.z = 0
		if self.direction == 2:
			move_cmd.linear.x = -0.2
			move_cmd.angular.z = 0
		if self.direction == 3:
			move_cmd.linear.x = 0
			move_cmd.angular.z = 0.2
		if self.direction == 4:
			move_cmd.linear.x = 0
			move_cmd.angular.z = -0.2
		
		while not rospy.is_shutdown():
			self.cmd_vel.publish(move_cmd)
			
if __name__ = '__main__':
	Move(1)