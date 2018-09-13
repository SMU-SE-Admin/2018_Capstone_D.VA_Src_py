#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys, io
sys.path.append('/home/turtlebot/testing/2018_Capstone_D.VA_Src_py/module/image module/imagenet')
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import socket
import base64
import numpy
import time
import classify_image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Find_object_name:

  def __init__(self):
    port = 5010
    self.sock = socket.socket()
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind(('',port))
    self.sock.listen(10)
    print("wait client-----------------------------------")
    self.cli, info = self.sock.accept()
    print("client done-----------------------------------")
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/rgb/image",Image,self.callback)
    rospy.init_node('Find_object_name', anonymous=True)

  def callback(self,data):
    try:
      frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
      print("convert frame")
      encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
      result, imgencode = cv2.imencode('.png', frame, encode_param)
      data_img = numpy.array(imgencode.tobytes())
      print("make picture")
      classify_image.start(data_img)
      #time.sleep(10)
      print("classify done")
      print(classify_image.result)
      result = str(classify_image.result[0]).split(",")[0]
#      self.cli.send(str(classify_image.result[0])+":::")
      self.cli.send(result+":::")
      self.image_sub.unregister()
      self.cli.close()
      self.sock.close()
      print("search end!!!!!!!!!!!!")
    except CvBridgeError as e:
      print(e)

def main(args):
  ic = Find_object_name()
  print ("--------------find done----------")
  #rospy.spin()
  time.sleep(15)
  print ("searchobject end")
  sys.exit(0)

if __name__ == '__main__':
    main(sys.argv)
