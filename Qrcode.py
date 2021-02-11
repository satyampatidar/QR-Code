# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:20:24 2021

@author: Win Cartell Satyam Patidar
"""
# Import
import qrcode

# Creation of QR Code
img = qrcode.make("satyampatidar.github.io")

# Saving Code
img.save("qr.jpg") # Check the image in your working directory

# Reading

import cv2

d = cv2.QRCodeDetector()

# Reading using OpenCV
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("qr.jpg"))

print(val)
