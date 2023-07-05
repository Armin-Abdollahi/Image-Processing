clc;
clear all;

%% Read the image and convert to grayscale
image = imread('cameraman.jpg');
Grayscale_Image = im2gray(image);

%% Create and apply a Gaussian filter to the original image
sigma = 3;
B = imgaussfilt(Grayscale_Image,sigma);

%% Apply a noise to the filtered image
noisy_image = imnoise(B,'gaussian',0,0.025);

%% Apply the Wiener Filter to the noisy image
K = wiener2(noisy_image, [5,5]);

%% Display the original image and the noisy image and restored image
subplot(1,4,1);
imshow(Grayscale_Image);
title('Original Picture');

subplot(1,4,2);
imshow(B);
title('Degradation Function');

subplot(1,4,3);
imshow(noisy_image);
title('Noisy Image');

subplot(1,4,4);
imshow(K);
title('Wiener Filter');