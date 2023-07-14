image = imread('cameraman.jpg');
noisy_image = imnoise(image,'salt & pepper',0.05);

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