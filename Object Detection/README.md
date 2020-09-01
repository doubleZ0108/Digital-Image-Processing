# 目标检测

* [Recognition Based On Decision-Theoretic Methods](#recognition-based-on-decision-theoretic-methods)
* [Matching](#matching)
   * [Minimum Distance Classifier | 最小距离分类器](#minimum-distance-classifier--最小距离分类器)
   * [Coorelation | 相关](#coorelation--相关)
* [Optimum Statistical Classifiers](#optimum-statistical-classifiers)
   * [Gaussian Pattern Class](#gaussian-pattern-class)
* [Neural Networks](#neural-networks)

------

## Recognition Based On Decision-Theoretic Methods

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

**把x错判成$\omega_j$导致的平均loss**
$$
r_{j}(x)=\sum_{k=1}^{W} L_{k j} p\left(\omega_{k} / x\right) \\
=\frac{1}{p(x)} \sum_{k=1}^{W} L_{k j} p\left(x / \omega_{k}\right) p\left(\omega_{k}\right) \\ =\sum_{k=1}^{W} L_{k j} p\left(x / \omega_{k}\right) p\left(\omega_{k}\right)
$$

### Gaussian Pattern Class

$$
p\left(x / \omega_{j}\right)=\frac{1}{(2 \pi)^{n / 2}\left|C_{j}\right|^{1 / 2}} e^{-\frac{1}{2}\left(x-m_{j}\right)^{T} C_{j}^{-1}\left(x-m_{j}\right)}
$$

- $m_j = E_j{x}$ 均值
- $C_j = E_j{(x-m_j)(x-m_j)^T}$ 协方差

------

- $P(\omega_i) = \frac{1}{\omega}, C_i = \sigma^2I$
  $$
  d_i(x)=\frac{1}{2\sigma^2}||x-\omega^2||^2
  $$

  - $P(\omega_i) = \frac{1}{\omega}, C_i = C$ 	考虑了协方差

  $$
  d_i(x) = \frac{1}{2}(x-m_i)^TC_i^{-1}(x-m_i) \\
   = x^TC_i^{-1}m_i-\frac{1}{2}m_i^TC_i^{-1}m_i
  $$

------

## Neural Networks