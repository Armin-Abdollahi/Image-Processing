#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image

# Read the image
i = Image.open("cameraman.jpg")

# Image quantization with different qualities
i.save('Quality 35.jpg', quality=35)
i.save('Quality 10.jpg', quality=10)
i.save('Quality 5.jpg', quality=5)

# Display images
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(plt.imread('Quality 35.jpg'))
axs[0].set_title('Quality 35')
axs[1].imshow(plt.imread('Quality 10.jpg'))
axs[1].set_title('Quality 10')
axs[2].imshow(plt.imread('Quality 5.jpg'))
axs[2].set_title('Quality 5')
plt.show()

