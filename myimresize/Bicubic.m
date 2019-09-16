% ======================== bicubic ================================ %
function result_img = Bicubic(origin_img, result_img, origin_size, target_size, scale, type)
% 双三次插值法（Bicubic Interpolation Algorithm）
[oh,ow,od] = size(origin_img);
zmf = scale; %缩放因子

% initial target image TI
th = round(oh*zmf);
tw = round(ow*zmf);

% add original image with 2 rows and 2 cols
% expand the border to prevent calculation overflow
a = origin_img(1,:,:); b = origin_img(oh,:,:);
temp_I = [a;a;origin_img;b;b];
c = temp_I(:,1,:); d = temp_I(:,ow,:);
FI = [c,c,temp_I,d,d];

% fill target image with new pixels
for w = 1:tw
    j = floor(w/zmf)+2; v = rem(w,zmf)/zmf;
    for h = 1:th
        i = floor(h/zmf)+2;  u = rem(h,zmf)/zmf; 
        A = [s(u+1),s(u),s(u-1),s(u-2)];
        C = [s(v+1);s(v);s(v-1);s(v-2)];
        for d = 1:od   % image's 3 channels    
            try
                B = double(FI(i-1:i+2,j-1:j+2,d));
                result_img(h,w,d) = (A*B*C);    
            end
        end
    end
end


end

function w = s(wx)
% 插值核函数

wx = abs(wx);
if wx<1
    w = 1 - 2*wx^2 + wx^3;
elseif wx>=1 && wx<2
    w = 4 - 8*wx + 5*wx^2 - wx^3;
else
    w = 0;

end

end
% ======================== bicubic ================================ %