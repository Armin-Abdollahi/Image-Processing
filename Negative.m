i = imread('cameraman.jpg');
imshow(i);
h = imhist(i);
figure;
bar(h);
title('Histogram of Original');

figure;
c = imcomplement(i);
imshow(c);
h2 = imhist(c);
figure;
bar(h2);
title('Histogram of Negative');