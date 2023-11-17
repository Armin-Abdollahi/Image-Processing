#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an RGB image
RGB = cv2.imread('Azadi_Square.jpg')

# Convert RGB image to grayscale
I = cv2.cvtColor(RGB, cv2.COLOR_BGR2GRAY)

# Normalize the grayscale image to 128 levels
I_128 = np.uint8(I * (128 / 256))

# Normalize the grayscale image to 64 levels
I_64 = np.uint8(I * (64 / 256))

# Display the results
plt.figure(figsize=(15, 8))
plt.subplot(1, 3, 1), plt.imshow(cv2.cvtColor(RGB, cv2.COLOR_BGR2RGB)), plt.title('Original RGB Image'), plt.axis("off")
plt.subplot(1, 3, 2), plt.imshow(I_128, cmap='gray'), plt.title('Grayscale (128 levels)'), plt.axis("off")
plt.subplot(1, 3, 3), plt.imshow(I_64, cmap='gray'), plt.title('Grayscale (64 levels)'), plt.axis("off")
plt.show()

