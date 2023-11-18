#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('cameraman.jpg')

# Convert RGB image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply salt noise to the original image
noisy_image = np.copy(gray_image)
noise = np.random.rand(*gray_image.shape)
noisy_image[noise > 1 - 0.5/2] = 255

# Apply min filter to the noisy image
filtered_image = cv2.erode(noisy_image, np.ones((3, 3)), iterations=1)

# Display images
plt.figure(figsize=(15, 8))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')

plt.show()

