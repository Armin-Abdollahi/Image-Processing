# Image-Processing-Filtering

Image Processing filters in MATLAB & Python

https://github.com/user-attachments/assets/4ea1b55e-f6b1-42cd-983c-fecdabf42fc5

You can see the Tutorial video of the Image Processing Filters on my YouTube channel:
https://www.youtube.com/watch?v=fRVrkqmvTgM&t=2559s

In this video, we will explore the world of image processing filters using MATLAB and Python. We will start by understanding the basics of image processing and how filters can be used to enhance and manipulate images. 

We will then dive into the different types of filters such as Gaussian, Median, and Sobel filters, and learn how to implement them in both MATLAB and Python. We will also discuss the importance of choosing the right filter for specific image processing tasks.

Throughout the video, we will provide step-by-step tutorials on how to apply these filters to real-world images and demonstrate their effects on image quality and features. Additionally, we will compare the results obtained from both MATLAB and Python implementations.

By the end of this video, you will have a solid understanding of image processing filters and be able to confidently apply them to your own projects using either MATLAB or Python. Whether you are a beginner or an experienced programmer, this video will provide valuable insights into the world of image processing.


---

### Edge Detection in Image Processing

Edge detection is a crucial technique in image processing that aims to identify and highlight significant transitions in intensity within an image, marking the boundaries of objects and features. By detecting edges, we can extract important structural information that is essential for various applications, such as object recognition, image segmentation, and scene understanding. In this repository, we explore several popular edge detection methods, including Sobel, Prewitt, Roberts, Laplacian of Gaussian (LoG), Zero-Crossing, and Canny algorithms. Each method employs different mathematical approaches to enhance edges and suppress noise, allowing users to compare their effectiveness visually. Through the application of these techniques on a classic image, we provide insights into how each algorithm performs under different conditions, showcasing the versatility and importance of edge detection in fields like computer vision, robotics, and medical imaging. This exploration not only emphasizes the significance of edges in image analysis but also serves as a foundation for more advanced image processing tasks.

![Screenshot (2190)](https://github.com/user-attachments/assets/5400fc56-5aae-4925-990b-dcf391cd8ac2)



### Gaussian Filter in the Frequency Domain

Gaussian filtering in the frequency domain is an advanced image processing technique that leverages the Fourier transform to enhance images by reducing noise and blurring. This method involves transforming an image into its frequency components, where different frequencies represent various details and structures within the image. By applying a Gaussian filter in this transformed space, we can selectively attenuate high-frequency noise while preserving important low-frequency information, effectively smoothing the image. After filtering, the inverse Fourier transform is used to reconstruct the image back into the spatial domain. This approach not only provides a powerful means of image restoration but also offers insights into the frequency characteristics of images. In this repository, we demonstrate Gaussian filtering in the frequency domain using a classic image, showcasing both the original and the restored versions. This technique is widely applicable in fields such as medical imaging, remote sensing, and computer vision, where clarity and detail are crucial for accurate analysis and interpretation.
Explore the code and experiment with different parameters to see how they affect the filtering process!

![Screenshot (2193)](https://github.com/user-attachments/assets/0aaee268-9351-411b-8052-4331cca561ec)



### Histogram Adjustment

Histogram adjustment is a powerful technique in image processing that enhances the contrast of images by redistributing pixel intensity values. This code implements a histogram equalization algorithm that effectively stretches the range of intensity values, improving the visibility of features in both bright and dark areas of an image. By applying this method, users can achieve a more balanced representation of their images, making it particularly useful for applications in photography, medical imaging, and remote sensing. The implementation is straightforward and can be easily integrated into your projects, allowing for quick adjustments to enhance image quality.

![Screenshot (2196)](https://github.com/user-attachments/assets/151a13c1-0543-4623-b919-ae7bdab6873a)



### Histogram Matching

Histogram matching is an essential technique in image processing that aims to transform the pixel intensity distribution of one image to match that of another reference image. This code provides a robust implementation of histogram matching, allowing users to seamlessly adjust the tonal characteristics of their images to achieve a desired look or to standardize images for analysis. By aligning the histograms, this method enhances visual consistency across a set of images, making it particularly useful in fields such as medical imaging, computer vision, and photography. The straightforward interface and efficient algorithm make it easy to integrate into your projects, enabling you to elevate the quality and coherence of your visual data effortlessly.

![Screenshot (2199)](https://github.com/user-attachments/assets/1b0e4d01-f070-4a42-87cf-20759886ff82)



### Inverse Filtering in Image Processing

Inverse filtering is a powerful technique used in image processing to restore images that have been degraded by various factors, such as noise or blurring. This method operates on the principle of reversing the effects of a degradation function, allowing for the recovery of the original image as closely as possible. In this repository, we explore the application of inverse filtering through a practical example, where an image is first converted to grayscale and subjected to Gaussian noise. By applying an unsharp filter as part of the inverse filtering process, we aim to enhance the visual quality of the noisy image. This approach not only demonstrates the effectiveness of inverse filtering but also highlights its significance in various fields, including photography, medical imaging, and remote sensing, where clarity and detail are paramount.

![Screenshot (2202)](https://github.com/user-attachments/assets/2dad0b80-af0a-4533-969b-42b30fdbc0d6)



### Negative Image Transformation

Negative image transformation is a fundamental technique in image processing that involves inverting the pixel values of an image. This process creates a visual effect where dark areas become light and vice versa, effectively producing a "negative" of the original image. The transformation is particularly useful for enhancing contrast and revealing details that may be obscured in the original representation. In this repository, we demonstrate the negative transformation using a classic image, showcasing both the original and its negative counterpart. Additionally, we provide a histogram analysis for both images, allowing users to visualize how pixel intensity distributions change after inversion. This technique finds applications in various domains, including artistic photography, medical imaging, and scientific analysis, where it can aid in highlighting features that are otherwise difficult to discern.

![Screenshot (2209)](https://github.com/user-attachments/assets/f0a95ad9-213a-4dbd-888b-d91c3056c7c1)



### Wiener Filtering in Image Restoration

Wiener filtering is a sophisticated technique in image processing designed to enhance the quality of images that have been degraded by noise. Named after the mathematician Norbert Wiener, this adaptive filtering method aims to minimize the mean square error between the estimated and the original image. By analyzing local image statistics, Wiener filtering effectively distinguishes between noise and actual image content, allowing for a more precise restoration. In this repository, we illustrate the application of the Wiener filter on a noisy grayscale image, demonstrating its ability to recover details that are often lost due to Gaussian noise. This technique is particularly valuable in fields such as medical imaging, satellite imagery, and photography, where maintaining clarity and detail is essential for accurate analysis and interpretation. Through visual comparisons of the original, noisy, and restored images, users can appreciate the effectiveness of Wiener filtering in practical scenarios.

![Screenshot (2211)](https://github.com/user-attachments/assets/f275d0af-f800-4b2d-833f-5c5ab3adadfb)
