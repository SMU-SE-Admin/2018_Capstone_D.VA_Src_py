#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import socket
import base64
import numpy
import time
import os

class Find_object_name:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/rgb/image",Image,self.callback)

    pro = os.path.join(os.path.dirname(os.path.abspath(__file__)),"ip.txt")
    f = open(pro, "r")
    self.ip = f.readline()
    f.close()
    self.port = 5009
    self.sock = socket.socket()
    self.sock.bind(('',self.port))
    self.sock.listen(10)
    self.cli, info = self.sock.accept()


  def callback(self,data):
    try:
      frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    self.image_sub.unregister()
    self.cli.send("test")
    self.cli.close()
    self.sock.close()

def main(args):
  ic = Find_object_name()
  rospy.init_node('Find_object_name', anonymous=True)

if __name__ == '__main__':
    main(sys.argv)
