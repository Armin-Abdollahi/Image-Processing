#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('cameraman.jpg')

# Generate Gaussian noise
noise = np.zeros(img.shape, img.dtype)
cv2.randn(noise, 0, 150) # mean = 0, standard deviation = 150

# Add the noise to the image
noisy_img = cv2.add(img, noise)

# Define the mean filter
w = np.ones((3, 3)) / 9

# Apply the mean filter to the noisy image
gd = cv2.filter2D(noisy_img, -1, w)


# Display the images
plt.figure(figsize=(15, 8))
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_img)
plt.title('Image with Gaussian noise')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(gd)
plt.title('After applying the mean filter to the noisy image')
plt.axis('off')

plt.show()

