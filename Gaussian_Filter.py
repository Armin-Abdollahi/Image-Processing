#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

# Read the image
img = cv2.imread('cameraman.jpg')

# Create gaussian filter
filter_size = (5, 5)
sigma = 3
gaussian_filter = cv2.getGaussianKernel(filter_size[0], sigma) * cv2.getGaussianKernel(filter_size[1], sigma).T

# Applying the Gaussian filter to the shifted Fourier transform
filtered_image = cv2.filter2D(img, -1, gaussian_filter)

# Display the original image and the reconstructed image
cv2.imshow('Original Picture', img)
cv2.imshow('Filtered Picture', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

