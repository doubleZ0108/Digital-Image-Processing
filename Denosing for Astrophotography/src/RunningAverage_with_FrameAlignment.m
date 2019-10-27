clear;
clc;

video_path = 'Resources/';
result_path = 'ScreenShots/';
video_name = 'hw1_sky_2.avi';
result_name = 'hw1_sky_2_frame.png';
result_average_name = 'hw1_sky_2_frame_shift_10.png';

vidobj = VideoReader([video_path,video_name]); 

%% loop
frame_average_last = im2double(read(vidobj, 1));
for t=2:30
    t
    frame_now = im2double(read(vidobj, t));
    frame_average = (t-1)/t * frame_average_last + 1/t * Align(frame_now, frame_average_last);
    frame_average_last = frame_average;
end

% figure;
% imshow(frame_now, []);
% figure;
% imshow(frame_average, []);
imwrite(frame_average, [result_path, result_average_name]);


function frameTform = imshift(frame, dx, dy)
% shift the img where
% move right dx
% move up dy

A = [1 0 0; 0 1 0; dx dy 1];
tform = maketform('affine', A);
[height, width, channels] = size(frame);
frameTform = imtransform(frame, tform, 'bilinear', ...
                            'XData', [1 width], ...
                            'YData', [1 height], ...
                            'FillValues', zeros(channels, 1));

end

function min_msd_frame = Align(f, g)
% aligns frames f and g by minimizing the mean squared difference 
% over a set of horizontal and vertical shifts. 

[M,N,type] = size(f);

% initialize min_msd_frame with the origin frame
diff = f - g;
min_msd = sum(sum(diff .^ 2)) / (M * N);
min_msd_frame = f;
min_index = [0, 0];

n = 10;     % user-defined

% loop the shift choices
% choose the smallest mean squared differences among the averaged frame
for dx=-n:n
    for dy=-n:n
        
        shifted_f = imshift(f, dx, dy);
        [M,N,type] = size(shifted_f);
        
        % crop the shifted frame
        rowl = 1; rowr = M + dy;
        colt = dx + 1; colb = N;
        if rowr > M, rowr = M; end
        if colt < 1, colt = 1; end
        
        sub_f = shifted_f(rowl:rowr, colt:colb, type);
        sub_g = g(rowl:rowr, colt:colb, type);
        
        % calculate the mean square difference
        diff = sub_f - sub_g;
        [M,N,type] = size(sub_f);
        msd = sum(sum(diff .^ 2)) / (M * N);
        
        % update to the smallest one
        if msd < min_msd
            min_msd = msd;
            min_msd_frame = shifted_f;
            min_index = [dx, dy];
        end
        
    end
end

end