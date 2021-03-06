% ======================== nearest ================================ %
function result_img = Nearest(origin_img, result_img, origin_size, target_size, scale, type)
% 最近邻域内插法(Nearest Neighbor Interpolation Algorithm)

for x=1:target_size(1)
    for y=1:target_size(2)
        
        % 将result中的每个像素位置对应到origin中
        a = (x+0.5) / scale + 0.5;
        b = (y+0.5) / scale + 0.5;
        
        % 找到最近的四个像素位置
        [a1,a2,b1,b2] = growNearest(a, b, origin_size(1), origin_size(2));
        
        % 寻找四个位置中距离插值点最近的位置
        D = [distance(a,b,a1,b1),distance(a,b,a1,b2),distance(a,b,a2,b1),distance(a,b,a2,b2)];
        [min_x, min_y] = findMinPos(a1,a2,b1,b2,D);
        
        for z=1:type
             try
                 % 将这个点的像素赋予插值点
                 result_img(x,y,z) = origin_img(min_x,min_y,z);
             end
        end
        
    end
end


end

function [a1,a2,b1,b2] = growNearest(a, b, width, height)
% 找到附近的4个位置（边界检查）

a1 = round(a);
if a1>width-1, a1 = width-1; end
a2 = a1 + 1;

b1 = round(b);
if b1>height-1, b1 = height-1; end
b2 = b1 + 1;

end

function length = distance(x, y, a, b)
% 返回点(x,y)到点(a,b)的欧拉距离平方
% 只需要比较距离大小进行选择，这里省去开根运算

length = (x-a)^2 + (y-b)^2;

end

function [min_x, min_y] = findMinPos(a1,a2,b1,b2,D)
% 找出距插值点最近位置
% D矩阵存储周围点到插值点的位置

minindex = find(D==max(D));

switch(minindex(1))     % 可能有多个最近值，这里选择第一个
    case 1
        min_x = a1;
        min_y = b1;
    case 2
        min_x = a1;
        min_y = b2;
    case 3
        min_x = a2;
        min_y = b1;
    case 4
        min_x = a2;
        min_y = b2;
end

end
% ======================== nearest ================================ %