rgb_img = imread('../Resources/tongji.png');
grey_img = rgb2gray(rgb_img);

salt_pepper_noise_img = imnoise(grey_img, 'salt & pepper', 0.5);        % 噪声密度为0.5

% Median Filter
median_restoration_img = medfilt2(salt_pepper_noise_img);
% imshowpair(salt_pepper_noise_img, median_restoration_img, 'montage');

% Adaptive Median Filter
adaptivemedian_restoration_img = AdaptiveMedianFiltering(salt_pepper_noise_img, 10);
% imshowpair(salt_pepper_noise_img, adaptivemedian_restoration_img, 'montage');

subplot(1,3,1);
imshow(salt_pepper_noise_img);
subplot(1,3,2);
imshow(median_restoration_img);
subplot(1,3,3);
imshow(adaptivemedian_restoration_img);

function MedianFiltering(noise_img)
end

function restoration_img = AdaptiveMedianFiltering(noise_img, MaxSize)
S_max = MaxSize;
[M,N] = size(noise_img);

% 扩展图像
img = zeros(M+S_max*2, N+S_max*2,'uint8');
restoration_img = img;
img(S_max+1:M+S_max, S_max+1:N+S_max) = noise_img;

% 如果扩展位置用0填充，则图像边缘的噪声无法去除
img(1:S_max,S_max+1:S_max+N) = noise_img(1:S_max,1:N);      % 上边界
img(S_max+M+1:M+S_max*2,S_max+1:S_max+N) = noise_img(M-S_max+1:M,1:N);    % 下边界
img(S_max+1:S_max+M,1:S_max) = noise_img(1:M,1:S_max);  % 左边界
img(S_max+1:S_max+M,S_max+N+1:N+S_max*2) = noise_img(1:M,N-S_max+1:N);  % 右边界

for ii = S_max+1:S_max+M
    for jj = S_max+1:S_max+N
        
        window_size = 1;
        while window_size<=S_max
            neighbor = img(ii-window_size:ii+window_size, jj-window_size:jj+window_size);    % 获取临域
            neighbor = neighbor(:);  % 转化为列向量
            
            z_med = median(neighbor);
            z_min = min(neighbor);
            z_max = max(neighbor);
            
            if z_min<z_med && z_med<z_max   % 当前临域中值不是噪声
                break;
            else
                window_size = window_size + 1;
            end
        end
        
        if z_min<img(ii,jj) && img(ii,jj)<z_max
            restoration_img(ii,jj) = img(ii,jj);    % 如果当前像素不是噪声，原值输出
        else
            restoration_img(ii,jj) = z_med;         % 如果当前像素是噪声，中值滤波
        end
        
    end
end

restoration_img = restoration_img(S_max+1:M+S_max, S_max+1:N+S_max);
end