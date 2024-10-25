clc;
clear all;

% Read the image
img = imread('cameraman.jpg');

% Fourier transform
fft_image = fft2(img);

% Shifted fourier transform
shifted_fft_image = fftshift(fft_image);

%% Create gaussian filter
filter_Size = [5,5];
sigma = 1;                 % Gaussian filter standard deviation parameter
guassianFilter = fspecial('gaussian',filter_Size,sigma);

%% Applying the Gaussian filter to the shifted Fourier transform
filteredImage = imfilter(shifted_fft_image,guassianFilter);

%% Return to the initial state
filtered_shifted_fft_image = ifftshift(filteredImage);

%% Image reconstruction using inverse Fourier transform
reconstructed_image = ifft2(filtered_shifted_fft_image);

%% Display the original image and the reconstructed image

subplot(2,3,1);
imshow(img);
title('Original Picture');

subplot(2,3,2);
imshow(fft_image);
title('Fourier transform');

subplot(2,3,3);
imshow(shifted_fft_image);
title('Shifted fourier transform');

subplot(2,3,4);
imshow(filteredImage);
title('Applying the Gaussian filter');

subplot(2,3,5);
imshow(filtered_shifted_fft_image);
title('Inverse shifted fourier transform');

subplot(2,3,6);
imshow(reconstructed_image);
title('Restored Picture');
