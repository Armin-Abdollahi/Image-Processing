#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image and convert to grayscale
image = cv2.imread('Azadi_Square.jpg')
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create and apply a Gaussian filter to the original image
sigma = 3
blurred_image = cv2.GaussianBlur(grayscale_image, (0, 0), sigma)

# Apply noise to the filtered image
noisy_image = blurred_image + np.random.normal(0, 10, blurred_image.shape)

# Apply the Inverse Filter to the noisy image
filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
filtered_image = cv2.filter2D(noisy_image, -1, filter)

# Display the original image, grayscale image, blurred image, noisy image, and filtered image
plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Picture')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Picture')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(blurred_image, cmap='gray')
plt.title('Degradation Function')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(filtered_image, cmap='gray')
plt.title('Inverse Filter')
plt.axis('off')

plt.show()

