clc;
clear all;

%% Read the image and convert to grayscale
image = imread('Azadi_Square.jpg');
Grayscale_Image = im2gray(image);

%% Create and apply a Gaussian filter to the original image
sigma = 3;
B = imgaussfilt(Grayscale_Image,sigma);

%% Apply a noise to the filtered image
noisy_image = imnoise(B,'gaussian',0,0.025);

%% Apply the Wiener Filter to the noisy image
K = wiener2(noisy_image, [5,5]);

%% Display the original image and the noisy image and restored image
subplot(2,3,1);
imshow(image);
title('Original Picture');

subplot(2,3,2);
imshow(Grayscale_Image);
title('Grayscale Picture');

subplot(2,3,3);
imshow(B);
title('Degradation Function');

subplot(2,3,4.5);
imshow(noisy_image);
title('Noisy Image');

subplot(2,3,5.5);
imshow(K);
title('Wiener Filter');