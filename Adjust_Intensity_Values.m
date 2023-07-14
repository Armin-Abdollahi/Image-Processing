i = imread('cameraman.jpg');      % Read the image
j = imadjust(i,[0 1],[1 0]);  % (image, [Low_in High_in], [Low_out High_out])

subplot(1,2,1);
imshow(i);
title('Original')

subplot(1,2,2);
imshow(j);
title('Adjusted')