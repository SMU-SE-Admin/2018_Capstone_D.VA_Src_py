import socket
import base64
import cv2
import numpy
import time
import os

f = open(os.path.join(os.getcwd(),"StringClassify","RobotControl","ip.txt"),"r")
ip = f.readline()
f.close()
port = 5005

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ret, frame = cap.read()
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
    sock.sendto(s, (ip, port))
    i = len(img)
    send_size = 1024
    offset = 0
    while i > 0:
        if i > send_size:
            buf = img[offset: offset + send_size]
            sock.sendto(buf, (ip, port))
            #time.sleep(0.005)
        else:
            buf = img[offset: offset + i]
            pend = 1024 - len(buf)
            for i in range(0, pend):
                buf = buf+"0"
            #print len(buf)
            sock.sendto(buf, (ip, port))
            time.sleep(0.005)
        offset += send_size
        i -= send_size