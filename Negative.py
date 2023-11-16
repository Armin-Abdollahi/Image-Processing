#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt

# Read the image
i = cv2.imread('cameraman.jpg', cv2.IMREAD_GRAYSCALE)

# Display the original image
plt.imshow(i, cmap='gray')
plt.title('Original Image')
plt.show()

# Calculate the histogram
h1 = cv2.calcHist([i], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.bar(range(256), h1.ravel())
plt.title('Histogram of Original')
plt.show()

# Create the negative image
c = cv2.bitwise_not(i)

# Display the negative image
plt.imshow(c, cmap='gray')
plt.title('Negative Image')
plt.show()

# Calculate the histogram for the negative image
h2 = cv2.calcHist([c], [0], None, [256], [0, 256])

# Plot the histogram for the negative image
plt.figure()
plt.bar(range(256), h2.ravel())
plt.title('Histogram of Negative')
plt.show()

