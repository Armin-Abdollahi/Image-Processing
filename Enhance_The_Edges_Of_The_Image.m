i = imread('cameraman.jpg');
w = (-1) * ones(3);
w(2,2)=5;
w(1,1)=0;
w(1,3)=0;
w(3,1)=0;
w(3,3)=0;
gd = imfilter(i,w);

subplot(1,2,1);
imshow(i);
title('Original Picture');

subplot(1,2,2);
imshow(gd,[]);
title('Adding Image Edges To The Image Itself')