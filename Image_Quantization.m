%% Read the image
i = imread("cameraman.jpg");

%% Image quantization with different qualities
imwrite(i,'Quality 35.jpg','Quality',35);
imwrite(i,'Quality 10.jpg','Quality',10);
imwrite(i,'Quality 5.jpg','Quality',5);

%% Display images
subplot(1,3,1);
i1 = imread ('Quality 35.jpg');
imshow(i1,[]);
title('Quality 35')

subplot(1,3,2);
i2 = imread ('Quality 10.jpg');
imshow(i2,[]);
title('Quality 10')

subplot(1,3,3);
i3 = imread ('Quality 5.jpg');
imshow(i3,[]);
title('Quality 5')