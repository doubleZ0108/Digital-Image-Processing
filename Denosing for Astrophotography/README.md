# Denoising for Astrophotography

[TOC]

------

## 1. Description

Amateur astrophotographers often set up static cameras pointed toward particular regions of the night sky and record for an extended period of time. Among the handouts, you can find two videos hw1 sky 1.avi and hw1 sky 2.avi, which contain two recordings of the night sky each lasting a few minutes. **Low light levels cause the video frames to be noticeably noisy.** 

------

## 2. Development Environment

- **Development Environment:** macOS Mojave 10.14.6
- **Development Software:** MATLAB_R2019a
- **Development Language:** Matlab

------

## 3. How To Run



------

## 4. Experiment

### a) Running average of the frames without frame alignment

#### Overall Thought of the Algorithm

According to the rules
$$
\begin{array}{l}{f_{\text {average}}^{1}=f^{1}} \\ {f_{\text {average}}^{t}=\frac{t-1}{t} f_{\text {average}}^{t-1}+\frac{1}{t} f^{t}, t=2,3, \ldots}\end{array}
$$
I found that  $f_{average}^{30}$ is based on $f_{average}^{t}$ and $f^{t}$

- $f^{t}$: the `t` frame of the video
- $f_{average}^{t}$: running average of the frames $f^{t}$ in the video without frame alignment, and it is given by a <u>recursive formula</u>
  - **Recursive termination condition:** the running average of the first frame is the first frame itself(because it haven't running, so we cannot calculate the average yet)
  - **Recursive expression:** $f_{average}^{t}$ is calcluate by weighted summation of $f_{average}^{t-1}$ and $f^{t}$, the weights is $\frac{t-1}{t}$ and $\frac{1}{t}$

#### Matlab Code

- **Loop version**

  ```matlab
  frame_average_last = im2double(read(vidobj, 1));    % first frame of the video
  for t=2:30
      frame_now = im2double(read(vidobj, t));
      frame_average = (t-1)/t * frame_average_last + 1/t * frame_now;     % weighted summation
      frame_average_last = frame_average;     % update the fresh frame
  end
  ```

- **Recursive version**

  ```matlab
  result = f_a(30, vidobj);
  imshow(result);
  
  function frame = f(t, vidobj)
  % return the "t"th frame of the video input
  
  frame = im2double(read(vidobj, t));
  
  end
  
  function frame = f_a(t, vidobj)
  % return the "t"th running average of the frames f_t 
  % without frame alignment
  
  if t==1
      frame = f(1, vidobj);
  else
      frame = (t-1)/t * f_a(t-1, vidobj) + 1/t * f(t, vidobj);
  end
  
  end
  ```

  



------

## 5. Realization

### 5.1.1 Some Function

#### 5.1.1 Overall Thought of the Algorithm

#### 5.1.2 Implementation Step

------

## 6. About the Author

| Item            | Info                     |
| --------------- | ------------------------ |
| **Name**        | Zhe Zhang(张喆)          |
| **ID**          | 1754060                  |
| **Adviser**     | Prof. Qingjiang Shi      |
| **Course Name** | Digital Image Processing |
| **Course Time** | Tue. 2-4 [1-17]          |
| **Email**       | doubleZ0108@163.com      |

------

## 7. Project Structure

```

```

------

