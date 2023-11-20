% Reading input image
input_image = imread('cameraman.jpg');

%% Checking if the image is already grayscale
if size(input_image, 3) == 3
    input_image = rgb2gray(input_image);
end

%% Saving the size of the input image in pixels
[M, N] = size(input_image);

%% Getting Fourier Transform of the input image
FT_img = fft2(double(input_image));

%% Assign Cut-off Frequency
D0 = 10; % one can change this value accordingly

%% Designing filter: Ideal High Pass Filter
u = 0:(M-1);
idx = find(u>M/2);
u(idx) = u(idx)-M;
v = 0:(N-1);
idy = find(v>N/2);
v(idy) = v(idy)-N;

%% MATLAB library function ndgrid (v, u) returns 2D grid which contains the coordinates of vectors v and u. Matrix V with each row is a copy of v and matrix U with each column is a copy of u.
[U, V] = ndgrid(u, v);

%% Calculating Euclidean Distance
D = sqrt(U.^2 + V.^2);

%% Determining the filtering mask
H = double(D > D0);

%% Check the dimensions of H and FT_img using the size function
[x, y] = size(H);
[x1, y1] = size(FT_img);

%% Convolution between the Fourier Transformed image and the mask
G = H.*FT_img;

%% Getting the resultant image by Inverse Fourier Transform of the convoluted image
output_image = real(ifft2(double(G)));

%% Displaying Input Image and Output Image
subplot(1,2,1);
imshow(input_image);
title('Original Image');

subplot(1,2,2);
imshow(output_image, []);
title('Ideal High Pass Filter');