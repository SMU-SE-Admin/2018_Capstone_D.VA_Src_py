import numpy
import cv2, io
from PIL import Image
from imagenet import classify_image
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

img = cv2.imread('C:\\Users\\KJH\\Desktop', cv2.IMREAD_COLOR)
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (640,480))

ret, frame = cap.read()

if ret:
    ret, frame = cap.read()
    percent = 25
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
    result, imgencode = cv2.imencode('.png', frame, encode_param)
    
    data_img = numpy.array(imgencode.tobytes())
    classify_image.start(data_img)
#    cv2.imshow("Image window", frame)
#    cv2.waitKey(0)
    print(classify_image.result)

cap.release()
out.release()
cv2.destroyAllWindows()