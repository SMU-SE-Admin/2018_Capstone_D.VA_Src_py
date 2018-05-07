#!/usr/bin/env python
from __future__ import print_function

import numpy
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from threading import Thread
import os
import sys
import array
import socket

class image_converter:
  def __init__(self):
    print("1")
    self.bridge = CvBridge()
    print("2")
    self.image_sub = rospy.Subscriber("/rgb/image",Image,self.callback)
    print("3")
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("4")
    self.s.bind(("",5001))
    print("5")
    self.s.listen(True)
    print("6")
    self.conn, addr = self.s.accept()
    print("7")
  
  #def send_img(self):
    

  def callback(self,data):
    try:
      print("8")
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      print("9")
      encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
      print("10")
      result, imgencode = cv2.imencode('.jpg', cv_image, encode_param)
      print("11")
      data_img = numpy.array(imgencode)
      print("!2")
      stringData = data_img.tostring()
      print("13")
      self.conn.send( str(len(stringData)).ljust(16));
      print("14")
      self.conn.send( stringData );
      print("done")
        #sock.close()

      decimg=cv2.imdecode(data_img,1)
      print("15")
    except CvBridgeError as e:
      print(e)
    print("16")
    cv2.imshow("Image window", decimg)
    print("17")
    cv2.waitKey(10)
    print("18")

if __name__ == '__main__':
  print("19")
  ic = image_converter()
  print("20")
  rospy.init_node('image_converter', anonymous=True)
  try:
    #while True:
     # ic.send_img()
    print("21")
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  print("22")
  cv2.destroyAllWindows()
