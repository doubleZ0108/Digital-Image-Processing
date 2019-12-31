# 目标检测

[TOC]

------

# Recognition Based On Decision-Theoretic Methods

## Matching

- 有一个pattern library，要做一个决策，$w \in \omega_?$，定义一组决策函数d，若$w \in \omega_i$，则$d_i > 所有其他的d_j$
- **decision boundary：**$d_i(x) = d_j(x)$
  - 要找到就是对于$\omega_i$，$d_{ij}(x)>0$；对于$\omega_j$，$d_{ij}<0$

### Minimum Distance Classifier | 最小距离分类器

用每一类的均值表征这一类，预测新值时，看与那个均值距离最近
$$
m_j = \frac{1}{N_j}\sum_{x\in \omega_j}x_j
$$
**欧几里得范数(二范数)**
$$
d_{j}(x)=x^{T} m_{j}-\frac{1}{2} m_{j}^{T} m_{j} \quad j=1,2, \ldots, W
$$

------

### Coorelation | 相关

$$
c(x, y)=\sum_{s} \sum_{t} w(s, t) f(x+s, y+t)
$$

**归一化**

寻找$\gamma(x,y)$最大值，得出最佳匹配位置
$$
\gamma(x, y)=\frac{\sum_{s} \sum_{t}[w(s, t)-w]\left[f(x+s, y+t)-\bar{f}_{x y}\right]}{\left\{\sum_{s} \sum_{t}[w(s, t)-w]^{2} \sum_{s} \sum_{t}\left[f(x+s, y+t)-\bar{f}_{x y}\right]^{2}\right\}^{\frac{1}{2}}}
$$

------

## Optimum Statistical Classifiers



------

## Neural Networks