% Reading input image
input_image = imread('cameraman.jpg');

%% Checking if the image is already grayscale
if size(input_image, 3) == 3
    input_image = rgb2gray(input_image);
end

%% Saving the size of the input image in pixels
[M, N] = size(input_image);

%% Getting Fourier Transform of the input image using MATLAB library function fft2 (2D fast fourier transform)
FT_img = fft2(double(input_image));

%% Assigning the order value
n = 2;

%% Assigning Cut-off Frequency
D0 = 10;

%% Designing filter: Butterworth High Pass Filter
u = 0:(M-1);
v = 0:(N-1);
idx = u > M/2;
u(idx) = u(idx) - M;
idy = v > N/2;
v(idy) = v(idy) - N;

%% MATLAB library function ndgrid (v, u) returns 2D grid which contains the coordinates of vectors v and u. Matrix V with each row is a copy of v and matrix U with each column is a copy of u.
[U, V] = ndgrid(u, v);

%% Calculating Euclidean Distance
D = sqrt(U.^2 + V.^2);

%% Determining the filtering mask
H = 1./(1 + (D0./D).^(2*n));

%% Check the dimensions of H and FT_img using the size function
[x, y] = size(H);
[x1, y1] = size(FT_img);

%% We used padarray function beceause the dimensions of the two arrays being multiplied do not match
pad_size = [x1-x, y1-y];
H_padded = padarray(H, pad_size, 'post');
resized_img = FT_img .* H_padded;

%% Convolution between the Fourier Transformed image and the mask
G = ifft2(resized_img);

%% Getting the resultant image by Inverse Fourier Transform of the convoluted image using MATLAB library function ifft2 (2D inverse fast fourier transform)
resultant_image = real(G);

%% Displaying the resultant image as output
subplot(1,2,1);
imshow(input_image);
title('Original Image');

subplot(1,2,2);
imshow(resultant_image, []);
title('Butterworth High Pass Filter');