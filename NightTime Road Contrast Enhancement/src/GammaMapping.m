clear;
clc;

img_path = 'Resources/';
imgs_name = ['hw1_dark_road_1.jpg';'hw1_dark_road_2.jpg';'hw1_dark_road_3.jpg'];
result_path = 'ScreenShots/Gamma Nonlinearity Mapping/';
[M,N] = size(imgs_name);

for k=3:3
    img_name = imgs_name(k,:);
    I = imread([img_path, img_name]);
    
%     figure;
    for gamma=0.4:0.1:1
        J = GammaNonlinearityMapping(I, gamma);
%         subplot(1,6,gamma*2); imshow(J);
        imwrite(J, [result_path, 'gammamapping_', num2str(gamma),'_', num2str(k), '.png']);
    end
end


function J = GammaNonlinearityMapping(I, gamma)

c = 255/(255^gamma);
% c = 1;

J = uint8(c*double(I).^gamma);

% x=0:0.1:255;
% y = c*x.^gamma;
% plot(x,y);
% hold on;

end