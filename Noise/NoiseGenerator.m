% 各种类型的噪声生成器

origin_img = imread('Resources/origin.png');

%% 高斯噪声
avg = 0;        % 均值
sigma = 25;     % 标准差
gaussian_noise_img = imnoise(origin_img, 'gaussian', avg, (sigma/255)^2);
% imshow(gaussian_noise_img);

%% 泊松分布噪声
poisson_noise_img = imnoise(origin_img, 'poisson');
% imshow(poisson_noise_img);

%% 椒盐噪声
noisy_density = 0.1;    % 噪声密度，大约有d*numel(img)个像素收到污染
salt_pepper_noise_img = imnoise(origin_img, 'salt & pepper', noisy_density);
% imshow(salt_pepper_noise_img);

%% 斑点噪声
% g = f + n*f
% n是均值为0，方差为sigma的均匀分布随机噪声
sigma = 0.1;
speckle_noise_img = imnoise(origin_img, 'speckle', sigma);
% imshow(speckle_noise_img)
