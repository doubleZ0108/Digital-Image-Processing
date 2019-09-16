% ======================== bilinear ================================ %
function result_img = Bilinear(origin_img, result_img, origin_size, target_size, scale, type)
% 双线性插值法 (Bilinear Interpolation Algorithm)

% 扩展原始图片矩阵边缘
tmp_img = zeros(origin_size(1)+2,origin_size(2)+2,type);
tmp_img(2:origin_size(1)+1,2:origin_size(2)+1,:) = origin_img;
tmp_img(1,2:origin_size(2)+1,:) = origin_img(1,:,:); tmp_img(origin_size(1)+2,2:origin_size(2)+1,:) = origin_img(origin_size(1),:,:);
tmp_img(2:origin_size(1)+1,1,:) = origin_img(:,1,:); tmp_img(2:origin_size(1)+1,origin_size(2)+2,:) = origin_img(:,origin_size(2),:);
tmp_img(1,1,:) = origin_img(1,1,:); tmp_img(1,origin_size(2)+2,:) = origin_img(1,origin_size(2),:);
tmp_img(origin_size(1)+2,1,:) = origin_img(origin_size(1),1,:); tmp_img(origin_size(1)+2,origin_size(2)+2,:) = origin_img(origin_size(1),origin_size(2),:);


% 由新图像某个像素(x,y) -映射-> 原始图像(ii,jj)处，并插值
for x=1:target_size(1)
    for y=1:target_size(2)
       ii = (x-1)/scale; jj = (y-1)/scale;
       i = floor(ii); j = floor(jj);
       u = ii-i; v = jj - j;
       i = i+1; j = j+1;
       result_img(x,y,:) = (1-u)*(1-v)*tmp_img(i,j,:) + (1-u)*v*tmp_img(i,j+1,:) + u*(1-v)*tmp_img(i+1,j,:) + u*v*tmp_img(i+1,j+1,:);
    end
end

end
% ======================== bilinear ================================ %