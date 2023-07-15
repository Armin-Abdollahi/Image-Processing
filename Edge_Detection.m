%% Read the image
i = imread("cameraman.jpg");

% Edge Detection
k=rgb2gray(i);
BW1 = edge(k,"sobel");
BW2 = edge(k,"prewitt");
BW3 = edge(k,"roberts");
BW4 = edge(k,"log");
BW5 = edge(k,"zerocross");
BW6 = edge(k,"canny");
BW7 = edge(k,'canny_old');
BW8 = edge(k,"approxcanny");

laplacian_filter = fspecial('laplacian');
f = imfilter(i,laplacian_filter);

%% Display images
subplot(2,5,1);
imshow(f);
title('Laplacian');

subplot(2,5,2);
imshow(BW1);
title('Sobel');

subplot(2,5,3);
imshow(BW2);
title('Prewitt');

subplot(2,5,4);
imshow(BW3);
title('Roberts');

subplot(2,5,5);
imshow(BW4);
title('Log');

subplot(2,5,6.5);
imshow(BW5);
title('Zerocross');

subplot(2,5,7.5);
imshow(BW6);
title('Canny');

subplot(2,5,8.5);
imshow(BW7);
title('Canny Old');

subplot(2,5,9.5);
imshow(BW8);
title('Approxcanny');