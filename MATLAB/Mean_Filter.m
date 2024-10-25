% Apply mean filter to image with Gaussian noise
i = imread('cameraman.jpg');
j = imnoise(i, 'gaussian', 0, 0.1);
w = ones(3) / (9);
gd = imfilter(j,w);

subplot(1,3,1);
imshow(i);
title('Original image');

subplot(1,3,2);
imshow(j);
title('Image with Gaussian noise');

subplot(1,3,3);
imshow(gd);
title('After applying the mean filter to the noisy image')
