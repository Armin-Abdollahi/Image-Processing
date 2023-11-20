% Read the input image
I = imread('cameraman.jpg');

%% Apply a 2-D Gaussian smoothing kernel with standard deviation sigma
sigma = 2;
G = fspecial('gaussian', [5 5], sigma);
I_smooth = imfilter(I, G, 'symmetric', 'conv'); % Also we can use imgaussfilt function => I_lowpass = imgaussfilt(I, sigma);

%% Subtract the smoothed image from the original image to obtain the high-pass filtered image
I_highpass = I - I_smooth;

%% Display the input image and the high-pass filtered image side by side
figure;
subplot(1, 2, 1);
imshow(I);
title('Input Image');

subplot(1, 2, 2);
imshow(I_highpass);
title('High-Pass Filtered Image');