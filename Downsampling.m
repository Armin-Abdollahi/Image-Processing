% Read the image
image = imread('Azadi_Square.jpg');

% Downsample by a factor of 1/2
downsampled_image_half = downsample(image, 2);

% Downsample by a factor of 1/4
downsampled_image_quarter = downsample(image, 4);

% Display the original and downsampled images
subplot(1, 3, 1);
imshow(image);
title('Original Image');

subplot(1, 3, 2);
imshow(downsampled_image_half);
title('Downsampled (1/2)');

subplot(1, 3, 3);
imshow(downsampled_image_quarter);
title('Downsampled (1/4)');