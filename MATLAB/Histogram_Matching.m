i = imread('lena_color_512.jpg');

sigma = 0.1;
h1 = imhist(i);
x = 1:256;
dh = 1 / sqrt(2*pi*sigma^2)*exp(-(x-100).^2/2*sigma^2);
j = histeq(i,dh);
h2 = imhist(j);

subplot(2,2,1);
imshow(i);
title('Original Picture');

subplot(2,2,2);
bar(h1);
title('Original Histogram');

subplot(2,2,3);
imshow(j);
title('Result');

subplot(2,2,4);
bar(h2)
title('Optimal Histogram');
