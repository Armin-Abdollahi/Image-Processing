#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

# Read the image
image = cv2.imread('Azadi_Square.jpg')

# Downsample by a factor of 1/2
downsampled_image_half = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)

# Downsample by a factor of 1/4
downsampled_image_quarter = cv2.resize(image, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_NEAREST)

# Display the original and downsampled images
cv2.imshow('Original Image', image)
cv2.imshow('Downsampled (1/2)', downsampled_image_half)
cv2.imshow('Downsampled (1/4)', downsampled_image_quarter)
cv2.waitKey(0)
cv2.destroyAllWindows()

