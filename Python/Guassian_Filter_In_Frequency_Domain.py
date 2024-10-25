#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import ndimage

# Read the image
img = cv2.imread('cameraman.jpg', 0)

# Fourier transform
fft_image = fftpack.fft2(img)

# Shifted fourier transform
shifted_fft_image = fftpack.fftshift(fft_image)

# Return to the initial state
filtered_shifted_fft_image = fftpack.ifftshift(shifted_fft_image)

# Image reconstruction using inverse Fourier transform
reconstructed_image = fftpack.ifft2(filtered_shifted_fft_image)

# Display the original image and the reconstructed image
plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Picture')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(fft_image.astype(np.uint8), cmap='gray')
plt.title('Fourier transform')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(shifted_fft_image.astype(np.uint8), cmap='gray')
plt.title('Shifted fourier transform')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(filtered_shifted_fft_image.astype(np.uint8), cmap='gray')
plt.title('Inverse shifted fourier transform')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(reconstructed_image.astype(np.uint8), cmap='gray')
plt.title('Restored Picture')
plt.axis('off')

plt.show()


# In[ ]:


import cv2
import numpy as np

# Reading the image
image = cv2.imread('lena_color_512.jpg', 0)  # 0 to read the image as grayscale

# Apply the Fourier transform
fft_image = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft_image)
magnitude_spectrum = 20 * np.log(np.abs(fft_shifted))

# Return to the original mode
ifft_shifted = np.fft.ifftshift(fft_shifted)
ifft_image = np.fft.ifft2(ifft_shifted)
restored_image = np.abs(ifft_image)

# Display images
cv2.imshow('Original Image', image)
cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))
cv2.imshow('Restored Image', restored_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

