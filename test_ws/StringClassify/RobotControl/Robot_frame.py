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

class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/rgb/image",Image,self.callback)

    pro = os.path.join(os.path.dirname(os.path.abspath(__file__)),"ip.txt")
    f = open(pro, "r")
    self.ip = f.readline()
    f.close()
    self.port = 5005
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def callback(self,data):
    try:
      frame = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    percent = 25
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
    result, imgencode = cv2.imencode('.png', frame, encode_param)
    data_img = numpy.array(imgencode)
    row_img = data_img.tostring()
    img = base64.standard_b64encode(row_img)
    print(len(img))
    s = str(len(img)) + ":::"
    s = s.zfill(1024)
    self.sock.sendto(s, (self.ip, self.port))
    i = len(img)
    send_size = 1024
    offset = 0
    while i > 0:
        if i > send_size:
            buf = img[offset: offset + send_size]
            self.sock.sendto(buf, (self.ip, self.port))
            #time.sleep(0.005)
        else:
            buf = img[offset: offset + i]
            pend = 1024 - len(buf)
            for i in range(0, pend):
                buf = buf+"0"
            #print len(buf)
            self.sock.sendto(buf, (self.ip, self.port))
            time.sleep(0.005)
        offset += send_size
        i -= send_size


def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
