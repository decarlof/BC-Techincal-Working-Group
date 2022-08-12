#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
How to grab images from a Panasonic iPro Extreme WV-S6130 web cam
"""

import os
import cv2
import pathlib
import json
import matplotlib.pyplot as plt
from dotenv import load_dotenv

def read_json(fname):
    with open(fname, 'r') as fp:
        alist = json.load(fp)
    return alist

# Create a file in the home directory called access.json
# {
#     "p"  : "password",
#     "u"  : "username",
#     'ip' : "192.168.1.1" # replace with the webcam IP address
# }


access_fname = os.path.join(str(pathlib.Path.home()), 'access.json')
access_dic = read_json(access_fname)

try:

    ret, frame = cv2.VideoCapture('http://' + access_dic['u'] +':' + access_dic['p'] + '@' + access_dic['ip'] + '/cgi-bin/mjpeg?stream=1').read()
    if ret:
        plt.imshow(frame)
        plt.show()

except FileNotFoundError:
    log.error('username and password are missing. Set them in a file called: %s' % access_fname )

