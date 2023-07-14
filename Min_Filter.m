% Read the image
image = imread('cameraman.jpg');

% Apply salt and pepper noise to the original image
noisy_image = imnoise(image,'salt & pepper',0.05);

% Apply min filter to the noisy image
filtered_image = ordfilt2(noisy_image, 1, true(3));

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