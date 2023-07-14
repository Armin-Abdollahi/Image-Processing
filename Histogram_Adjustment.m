i = imread('lena_color_512.jpg');

h1 = imhist(i);
g = histeq(i, 256);
h2 = imhist(g);

subplot(2,2,1);
imshow(i);
title('Original Picture');

subplot(2,2,2);
bar(h1);
title('Original Histogram');

subplot(2,2,3);
imshow(g);
title('Result');

subplot(2,2,4);
bar(h2);
title('Equalized Histogram');