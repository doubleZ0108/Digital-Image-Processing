clear;
clc;

video_path = 'Resources/';
result_path = 'ScreenShots/';
video_name = 'hw1_sky_1.avi';
result_name = 'hw1_sky_1_frame.png';
result_average_name = 'hw1_sky_1_frame_shift_3_1.png';

vidobj = VideoReader([video_path,video_name]); 

%% loop
frame_average_last = im2double(read(vidobj, 1));
for t=2:30
    frame_now = im2double(read(vidobj, t));
    frame_average = (t-1)/t * frame_average_last + 1/t * Align(frame_now, frame_average_last);
    frame_average_last = frame_average;
end

figure;
imshow(frame_now, []);
figure;
imshow(frame_average, []);


function frameTform = imshift(frame, dx, dy)
% dx = 1; % pixels
% dy = -1; % pixels
A = [1 0 0; 0 1 0; dx dy 1];
tform = maketform('affine', A);
[height, width, channels] = size(frame);
frameTform = imtransform(frame, tform, 'bilinear', ...
                            'XData', [1 width], ...
                            'YData', [1 height], ...
                            'FillValues', zeros(channels, 1));

end

function min_msd_frame = Align(f, g)

diff = f - g;
[M,N,type] = size(f);
min_msd = sum(sum(diff .^ 2)) / (M * N);
min_msd_frame = f;
min_index = [0, 0];

n = 3;
for dx=-n:n
    for dy=-n:n
        
        shifted_f = imshift(f, dx, dy);
        [M,N,type] = size(shifted_f);
        
        rowl = 1; rowr = M + dy;
        colt = dx + 1; colb = N;
        if rowr > M, rowr = M; end
        if colt < 1, colt = 1; end
        
        sub_f = shifted_f(rowl:rowr, colt:colb, type);
        sub_g = g(rowl:rowr, colt:colb, type);
        
        diff = sub_f - sub_g;
        [M,N,type] = size(sub_f);
        msd = sum(sum(diff .^ 2)) / (M * N);
        
        if msd < min_msd
            min_msd = msd;
            min_msd_frame = shifted_f;
            min_index = [dx, dy];
        end
        
    end
end

min_index

end