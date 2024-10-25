i = imread('lena_color_512.jpg');
w = [0 1 0;1 -4 1;0 1 0];
f2 = im2double(i);
g2 = imfilter(f2,w,'replicate');
g = f2-g2;

subplot(1,3,1);
imshow(i);
title('Original Picture');

subplot(1,3,2);
imshow(g2, []);
title('Laplacen Filter')

subplot(1,3,3);
imshow(g);
title('Adding Laplacian to the Original Image')
