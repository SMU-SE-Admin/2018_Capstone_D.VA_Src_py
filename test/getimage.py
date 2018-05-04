
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from socket import *
from threading import Thread
import os
import sys

class image_converter:
  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/rgb/image",Image,self.callback)
    
    self.s = socket(AF_INET, SOCK_STREAM)
    self.s.bind(("",12224))
    self.s.listen(10)
    self.conn, addr = self.s.accept()

  def send_img(self,img):
    self.conn.send(img.tobytes())

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    self.send_img(cv_image)
    
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

##class send_image:
##  def __init__(self):
##    self.s = socket(AF_INET, SOCK_STREAM)
##    self.s.bind(("",12224))
##    self.s.listen(10)
##    self.conn, addr = self.s.accept()
##
##  def send_img(img):
##    self.conn.send(img.tobytes())

if __name__ == '__main__':
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()
