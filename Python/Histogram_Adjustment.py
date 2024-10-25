#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('lena_color_512.jpg',cv2.IMREAD_GRAYSCALE)
h1 = cv2.calcHist([i], [0], None, [256], [0, 256])
g = cv2.equalizeHist(i)
h2 = cv2.calcHist([g], [0], None, [256], [0, 256])

plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
plt.title('Original Picture')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.bar(range(256), h1.ravel())
plt.title('Original Histogram')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title('Result')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.bar(range(256), h2.ravel())
plt.title('Equalized Histogram')

plt.show()

