% ======================== bicubic ================================ %
function result_img = Bicubic(origin_img, result_img, origin_size, target_size, scale, type)
% 双三次插值法（Bicubic Interpolation Algorithm）

m = origin_size(1); n = origin_size(2);

% 扩展原始图片矩阵边缘
FI = SpendImg(origin_img, origin_size, type);

% 使用BiCubic函数进行插值
for x=1:target_size(1)
    for y=1:target_size(2)
        i = floor(x/scale)+2;  u = rem(x,scale)/scale; 
        j = floor(y/scale)+2; v = rem(y,scale)/scale;
        
        A = [Ws(u+1),Ws(u),Ws(u-1),Ws(u-2)];
        C = [Ws(v+1);Ws(v);Ws(v-1);Ws(v-2)];
        
        for z = 1:type    
            try
                B = double(FI(i-1:i+2,j-1:j+2,z));
                result_img(x,y,z) = (A*B*C);    
            end
        end
        
    end
end

end

function w = Ws(wx)
% BiCubic插值函数

wx = abs(wx);
if wx<1
    w = 1 - 2*wx^2 + wx^3;
elseif wx>=1 && wx<2
    w = 4 - 8*wx + 5*wx^2 - wx^3;
else
    w = 0;

end

end

function tmp_img = SpendImg(origin_img, origin_size, type)
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

% ======================== bicubic ================================ %