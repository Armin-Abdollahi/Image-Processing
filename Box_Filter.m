i = imread('cameraman.jpg');
w = ones(3) / (9);
gd = imfilter(i,w);

subplot(1,2,1);
imshow(i);
title('Original Picture');

subplot(1,2,2);
imshow(gd);
title('Box Filter')