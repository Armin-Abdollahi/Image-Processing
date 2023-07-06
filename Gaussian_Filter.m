clc;
clear all;

% Read the image
img = imread('cameraman.jpg');

%% Create gaussian filter
filter_Size = [5,5];
sigma = 1;                 % Gaussian filter standard deviation parameter
guassianFilter = fspecial('gaussian',filter_Size,sigma);

%% Applying the Gaussian filter to the shifted Fourier transform
filteredImage = imfilter(img,guassianFilter);

%% Display the original image and the reconstructed image

subplot(1,2,1);
imshow(img);
title('Original Picture');

subplot(1,2,2);
imshow(filteredImage);
title('Filtered Picture');