% Read the image
img = imread('Azadi_Square.jpg');
 
% Upsample the image by a factor of 2 using nearest neighbor interpolation
upsampled_img = imresize(img, 2, 'nearest');
 
% Display the original and upsampled images
imshow(img);
title('Original Image');

figure;
imshow(upsampled_img);
title('Upsampled Image');
