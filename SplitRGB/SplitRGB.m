dirname = 'Resources/';
filename = 'her';
suffix = '.jpg';

% 读取图片文件
img = imread([dirname,filename,suffix]);

% 取RGB图片的三个通道
imgR = img(:,:,1);
imgG = img(:,:,2);
imgB = img(:,:,3);

% 绘制三个通道的图片
figure;
subplot(3,1,1);
imshow(imgR,[]);
subplot(3,1,2);
imshow(imgG,[]);
subplot(3,1,3);
imshow(imgB,[]);

% 将图片写出成jpg文件
imwrite(imgR,[dirname,filename,'_R',suffix]);
imwrite(imgG,[dirname,filename,'_G',suffix]);
imwrite(imgB,[dirname,filename,'_B',suffix]);