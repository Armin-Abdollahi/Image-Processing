i = imread("cameraman.jpg");
cr = i (130:400,120:400);

subplot(1,2,1);
imshow(i);
title('Original')

subplot(1,2,2);
imshow(cr);
title('Cropped')
