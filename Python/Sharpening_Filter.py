#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('cameraman.jpg')
w = np.full((3, 3), -1)
w[1, 1] = 5
w[0, 0] = 0
w[0, 2] = 0
w[2, 0] = 0
w[2, 2] = 0

gd = cv2.filter2D(i, -1, w)

plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
plt.title('Original Picture')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(gd, cv2.COLOR_BGR2RGB))
plt.title('After Applying The Filter')
plt.axis('off')

plt.show()

