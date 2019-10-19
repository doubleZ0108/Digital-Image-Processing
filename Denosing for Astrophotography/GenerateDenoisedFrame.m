clear;
clc;

video_path = 'Resources/';
result_path = 'ScreenShots/';
video_name = 'hw1_sky_2.avi';
result_name = 'hw1_sky_2_frame.png';
result_average_name = 'hw1_sky_2_frame_average.png';

vidobj = VideoReader([video_path,video_name]); 

%% loop
frame_average_last = im2double(read(vidobj, 1));
for t=2:30
    frame_now = im2double(read(vidobj, t));
    frame_average = (t-1)/t * frame_average_last + 1/t * frame_now;
    frame_average_last = frame_average;
end

figure;
subplot(1,2,1);
imshow(frame_now, []);
subplot(1,2,2);
imshow(frame_average, []);

% imwrite(frame_now, [result_path,result_name]);
% imwrite(frame_average, [result_path,result_average_name]);

%% Recursive
% result = f_a(30, vidobj);
% imshow(result);

function frame = f(t, vidobj)
frame = im2double(read(vidobj, t));
end

function frame = f_a(t, vidobj)

if t==1
    frame = f(1, vidobj);
else
    frame = (t-1)/t * f_a(t-1, vidobj) + 1/t * f(t, vidobj);
end

end