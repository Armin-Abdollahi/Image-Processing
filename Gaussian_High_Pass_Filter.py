#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
I = cv2.imread('cameraman.jpg')

# Apply a 2-D Gaussian smoothing kernel with standard deviation sigma

sigma = 2
G = cv2.getGaussianKernel(5, sigma)
G = np.outer(G, G.transpose())
I_smooth = cv2.filter2D(I, -1, G, borderType=cv2.BORDER_REFLECT)

# Subtract the smoothed image from the original image to obtain the high-pass filtered image
I_highpass = I - I_smooth

# Display the input image and the Gaussian high-pass filter image side by side
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
plt.imshow(I, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(I_highpass, cmap='gray')
plt.title('High-Pass Filtered Image')
plt.axis('off')

plt.show()

