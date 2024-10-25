#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

i = cv2.imread('cameraman.jpg')
w = np.ones((7, 7)) / 49
gd = cv2.filter2D(i, -1, w)

# Display Original and Box Filter
plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))
plt.title('Original Picture')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(gd, cv2.COLOR_BGR2RGB))
plt.title('Box Filter')
plt.axis('off')

plt.show()


# In[ ]:




