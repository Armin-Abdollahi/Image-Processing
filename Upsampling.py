#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('Azadi_Square.jpg')

# Upsample the image by a factor of 2 using nearest neighbor interpolation
upsampled_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)

# Display the original and upsampled images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(upsampled_img, cv2.COLOR_BGR2RGB))
plt.title('Upsampled Image')
plt.axis("off")

plt.show()

