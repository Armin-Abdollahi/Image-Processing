% Read the RGB image
I = imread('Azadi_Square.jpg');

% Convert the image from RGB to binary using thresholding
threshold = 0.7; % Adjust this threshold value as needed
J = im2bw(I, threshold);

% Display the input RGB image
subplot(1,2,1);
imshow(I);
title('Input RGB Image');

% Display the output binary image
subplot(1,2,2);
imshow(J);
title('Output Binary Image');