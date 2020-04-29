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
# Description : utils.py
# This file contains the code of the parameters and help functions
#
# *******************************************************************

import argparse

# -------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------

CONF_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4
IMG_WIDTH = 300
IMG_HEIGHT = 300
FRAME_WIDTH = 950

# Default colors
COLOR_RED = (0, 0, 255)

#RESNETSSD_FACEDETECTOR face detector based on SSD framework with reduced ResNet-10 backbone
#
# homepage = https://github.com/opencv/opencv/blob/3.4.0/samples/dnn/face_detector/how_to_train_face_detector.txt
#
# ## Model
#
# file = test/dnn/ResNetSSD_FaceDetector/deploy.prototxt
# url  = https://github.com/thegopieffect/computer_vision/blob/master/CAFFE_DNN/deploy.prototxt.txt
# size = 27.4 KB
# ## Weights
#
# file = test/dnn/ResNetSSD_FaceDetector/res10_300x300_ssd_iter_140000.caffemodel
# url  = https://github.com/thegopieffect/computer_vision/blob/master/CAFFE_DNN/res10_300x300_ssd_iter_140000.caffemodel
# size = 10.1 MB

# -------------------------------------------------------------------
# Help function
# -------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('--caffemodel', type=str, default='./data/weights/res10_300x300_ssd_iter_140000.caffemodel',
    help='path to caffemodel file')
parser.add_argument('--prototxt', type=str, default='./data/model/deploy.prototxt.txt',
    help='path to prototxt of model')
parser.add_argument('--video', type=str, default='vidoes/walking_in_uk.mp4',
    help='Path to video. Skip to capture real time from camera')
args = parser.parse_args()