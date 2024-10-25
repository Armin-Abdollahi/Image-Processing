#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from skimage import restoration
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, std=1):
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

# Read the image and convert to grayscale
original_image = cv2.imread('Azadi_Square.jpg')
grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply a noise to the Grayscale image
noisy_image = add_gaussian_noise(grayscale_image, mean=0, std=1)

# Apply the Wiener Filter to the noisy image
psf = np.ones((3, 3)) / 9
restored_image = restoration.wiener(noisy_image, psf, 0.001)

# Display the original image, grayscale image, noisy image, and the restored image
plt.figure(figsize=(15, 8))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Picture')
plt.axis('off')

# Display the grayscale image
plt.subplot(2, 2, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Picture')
plt.axis('off')

# Display the noisy image
plt.subplot(2, 2, 3)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

# Display the restored image
plt.subplot(2, 2, 4)
plt.imshow(restored_image, cmap='gray')
plt.title('Wiener Filter')
plt.axis('off')

# Show the figure
plt.show()

