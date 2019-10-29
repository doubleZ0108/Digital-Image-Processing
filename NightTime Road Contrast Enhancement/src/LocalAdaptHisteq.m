clear;
clc;

img_path = '../Resources/';
imgs_name = ['hw1_dark_road_1.jpg';'hw1_dark_road_2.jpg';'hw1_dark_road_3.jpg'];
result_path = 'ScreenShots/Local Adapt Histogram Equalization/';
[M,N] = size(imgs_name);

for k=1:M
    img_name = imgs_name(k,:);
    I = imread([img_path, img_name]);
    
    % adaptive histogram equalization
    numtiles = 16; cliplimit = 0.018;
    J = adapthisteq(I, ...
                    'NumTiles',[numtiles, numtiles], ...
                    'ClipLimit', cliplimit);
    imwrite(J, [result_path, 'adapthisteq_16_16_0.018_', num2str(k), '.png']);
end
