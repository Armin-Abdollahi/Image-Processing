#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt

# Read the image
i = cv2.imread("cameraman.jpg")

# Crop the region of interest
cr = i[130:400, 120:400]

# Display the original and cropped images
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cr, cv2.COLOR_BGR2RGB))
plt.title('Cropped')
plt.axis('off')

plt.show()

