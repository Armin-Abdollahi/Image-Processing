% Read an RGB image
RGB = imread('Azadi_Square.jpg');

% Convert RGB image to grayscale
I = rgb2gray(RGB);

% Normalize the grayscale image to 128 levels
I_128 = uint8(double(I) * (128 / 256));

% Normalize the grayscale image to 64 levels
I_64 = uint8(double(I) * (64 / 256));

% Display the results
subplot(1, 3, 1), imshow(RGB), title('Original RGB Image')
subplot(1, 3, 2), imshow(I_128), title('Grayscale (128 levels)')
subplot(1, 3, 3), imshow(I_64), title('Grayscale (64 levels)')
