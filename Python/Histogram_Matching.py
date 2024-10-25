#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
i = cv2.imread('Azadi_Square.jpg')

sigma = 0.1
h1, _ = np.histogram(i, bins=256)
x = np.arange(256)
dh = 1 / np.sqrt(2 * np.pi * sigma ** 2) * np.exp(-(x - 100) ** 2 / (2 * sigma ** 2))
j = np.interp(i, x, dh)
h2, _ = np.histogram(j, bins=np.arange(257))

plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
plt.title('Original Picture')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.bar(np.arange(256), h1)
plt.title('Original Histogram')

plt.subplot(2, 2, 3)
plt.imshow(j)
plt.title('Result')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.bar(np.arange(256), h2)
plt.title('Optimal Histogram')


plt.show()

