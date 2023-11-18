% Read image
image = imread('cameraman.jpg');

%% Convert RGB image to grayscale
gray_img = rgb2gray(image);

%% Add salt and pepper noise
noisy_image = imnoise(gray_img, 'salt & pepper', 0.2);

%% Apply median filter
filtered_image = medfilt2(noisy_image, [5,5]);

%% Display images
subplot(1,3,1);
imshow(image);
title('Original Picture');

subplot(1,3,2);
imshow(noisy_image);
title('Noisy Image');

subplot(1,3,3);
imshow(filtered_image);
title('After applying the median filter to the noisy image');