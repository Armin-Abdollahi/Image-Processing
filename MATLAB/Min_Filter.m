% Read the image
image = imread('cameraman.jpg');

% Convert RGB image to grayscale
gray_image = rgb2gray(image);

% Apply salt and pepper noise to the original image
noisy_image = imnoise(gray_image,'salt & pepper',0.05);

% Apply min filter to the noisy image
filtered_image = ordfilt2(noisy_image, 1, ones(3, 3), 'symmetric');


% Display images
subplot(1,3,1);
imshow(image);
title('Original Image');

subplot(1,3,2);
imshow(noisy_image);
title('Noisy Image');

subplot(1,3,3);
imshow(filtered_image);
title('Filtered Image');
