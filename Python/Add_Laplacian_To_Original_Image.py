#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('lena_color_512.jpg')
grayscale_image = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
w = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
g2 = cv2.filter2D(grayscale_image, -1, w, borderType=cv2.BORDER_REPLICATE)
g = grayscale_image - g2

plt.figure(figsize=(15, 8))
plt.subplot(1, 3, 1)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Original Picture')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(g2, cmap='gray')
plt.title('Laplacian Filter')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(g, cmap='gray')
plt.title('Adding Laplacian to the Original Image')
plt.axis('off')

plt.show()

