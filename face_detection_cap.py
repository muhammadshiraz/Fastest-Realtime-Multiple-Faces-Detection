# *******************************************************************
#
# Author : Muhammad Shiraz, 2020
# Email  : muhammadshiraz996@gmail.com
# Github : https://github.com/muhammadshiraz/
# Web    : www.muhammadshiraz.com
#
# Deep Neural Networks (DNNs)
# Face detection using the deep neural networks (dnn) module algorithm in OpenCV
#
# Description : face_detection_cap.py
# The main code of the Face detection using the deep neural networks (dnn) algorithm
#
# *******************************************************************

import cv2
import numpy as np
import imutils
from utils import *

# Give the configuration and model files to load the (dnn) network
net = cv2.dnn.readNetFromCaffe(args.prototxt, args.caffemodel)

if args.video:
    v_cap = cv2.VideoCapture(args.video)
else:
    v_cap = cv2.VideoCapture(0)

while True:
    # Capture video or webcam
    ret, frame = v_cap.read()
    frame = imutils.resize(frame, width=FRAME_WIDTH)

    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (IMG_WIDTH, IMG_HEIGHT)), 1.0,
        (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    # loop over the faces detections
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is correct
        if confidence < CONF_THRESHOLD:
            continue

        # compute the (x, y)-coordinates of the bounding box for the faces
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # draw a diagonal box for the faces and the associated force
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
            COLOR_RED, 2)
        cv2.putText(frame, text, (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, COLOR_RED, 2)

    # show output in the frame
    cv2.imshow("Fastest Multiple Faces Detection using the Deep Neural Networks (DNNs)", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, stop exploding
    if key == ord("q"):
        break

# do a bit of cleanup
cv2.destroyAllWindows()
v_cap.release()