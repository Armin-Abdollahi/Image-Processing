#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage.io import imread
from skimage import exposure
import matplotlib.pyplot as plt


i = imread('cameraman.jpg')
j = exposure.rescale_intensity(i, in_range=(0, 125), out_range=(0, 1))

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(i)
axs[0].set_title('Original')

axs[1].imshow(j)
axs[1].set_title('Adjusted')
plt.axis('off')

plt.show()

