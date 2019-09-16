% ======================== bilinear ================================ %
function result_img = Bilinear(origin_img, result_img, origin_size, target_size, scale, type)
% 双线性插值法 (Bilinear Interpolation Algorithm)

% 扩展原始图片矩阵边缘
extended_img = ExtendImg(origin_img, origin_size, type);

% 由新图像某个像素(x,y) -映射-> 原始图像(ii,jj)处，并插值
for x=1:target_size(1)
    for y=1:target_size(2)
        
       ii = (x-1)/scale; jj = (y-1)/scale;
       i = floor(ii); j = floor(jj);
       
       u = ii-i; v = jj - j;
       i = i+1; j = j+1;
       
%        result_img(x,y,:) = (1-u)*(1-v)*extended_img(i,j,:) + (1-u)*v*extended_img(i,j+1,:) + u*(1-v)*extended_img(i+1,j,:) + u*v*extended_img(i+1,j+1,:);
       
       U = [1-u, u];
       V = [1-v; v];
       
       for z=1:type
           F = [extended_img(i,j,z),extended_img(i,j+1,z);
               extended_img(i+1,j,z),extended_img(i+1,j+1,z)];
            
           try
               result_img(x,y,z) = (U*F*V);
           end
           
       end
      
    end
end

end

function tmp_img = ExtendImg(origin_img, origin_size, type)
% 将原始矩阵上下左右各包一层白边，并用相应的原始值填充

m = origin_size(1); n = origin_size(2);
tmp_img = zeros(m+2,n+2,type);              % 上下左右各添一个白边
tmp_img(2:m+1,2:n+1,:) = origin_img;        % 把原始图片放到正中间，上下左右为空
tmp_img(1,2:n+1,:) = origin_img(1,:,:);     % 原矩阵的第一行填充上边的空
tmp_img(m+2,2:n+1,:) = origin_img(m,:,:);   % 原矩阵的最后一行填充下边的空
tmp_img(2:m+1,1,:) = origin_img(:,1,:);     % 原矩阵的第一列填充左边的空
tmp_img(2:m+1,n+2,:) = origin_img(:,n,:);   % 原矩阵的最后一列填充右边的空
tmp_img(1,1,:) = origin_img(1,1,:);         % 左上角
tmp_img(1,n+2,:) = origin_img(1,n,:);       % 右上角
tmp_img(m+2,1,:) = origin_img(m,1,:);       % 左下角
tmp_img(m+2,n+2,:) = origin_img(m,n,:);     % 右下角

end
% ======================== bilinear ================================ %