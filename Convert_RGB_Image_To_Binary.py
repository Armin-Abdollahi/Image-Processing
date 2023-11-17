#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the RGB image
I = cv2.imread('Azadi_Square.jpg')

# Convert the image from RGB to binary using thresholding
threshold = 0.7 # Adjust this threshold value as needed
J = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
_, J = cv2.threshold(J, threshold*255, 255, cv2.THRESH_BINARY)

# Display the input RGB image
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title('Input RGB Image')
plt.axis('off')

# Display the output binary image
plt.subplot(1,2,2)
plt.imshow(J, cmap='gray')
plt.title('Output Binary Image')
plt.axis('off')

plt.show()

