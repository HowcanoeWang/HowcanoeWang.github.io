[toc]


# Part.1 行列式介绍

`行列式`：$det A$

`余因子式`：$C_{ij} = (-1)^{i+j} \cdot detA_{ij}$，其中，$A_{ij}$为矩阵$A$去掉$i$行$j$列剩下的元素组成的矩阵

`定理1`：nxn的矩阵可以用任意行或列的余因子展开式来计算，找到一行或一列合适的就行(含有0最多最简化计算量)

$$det A = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in} = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj}$$

`定理2`：若矩阵$A$为三角阵，则$det A$等于主对角线上面的元素乘积

$$A = \left[ \begin{matrix} a & \star & \star & \star \\ 0 & b & \star & \star \\ 0 & 0 & c & \star \\ 0 & 0 & 0 & d \end{matrix} \right] \rightarrow det A = a \cdot b \cdot c \cdot d$$	

拓展为：

$$U = \left[ \begin{matrix} \blacksquare & \star & \star & \star \\ 0 & \blacksquare & \star & \star \\ 0 & 0 & \blacksquare & \star \\ 0 & 0 & 0 & \blacksquare \end{matrix} \right] \rightarrow det U \neq 0$$

$$U = \left[ \begin{matrix} \blacksquare & \star & \star & \star \\ 0 & \blacksquare & \star & \star \\ 0 & 0 & 0 & \blacksquare \\ 0 & 0 & 0 & 0 \end{matrix} \right] \rightarrow det U = 0$$

`定理3`：(行变换)

令矩阵A是一个方阵

1. A的行倍加变换成为B，则$det A = det B$
2. A的两行对换成为B，则$det A = - det B$
3. A的某行乘以K成为B，则$det A = k \cdot det B$

`定理4`：当且仅当$det A \neq 0$，方阵A是可逆的

拓展：当矩阵行变换过程中，出现了两个一样的行或列，则$det A = 0$

`定理5`：若A为一个nxn方阵，则$det A^T = det A$

拓展：矩阵的行变换和列变换等价

`定理6`：乘法的性质

若A和B均为nxn方阵，则$det AB = (det A) (det B)$

拓展：通常情况下，$det (A+B) \neq det A + det B$

`行列式函数的先行性质`：把目光聚焦在矩阵的第j列，用向量x来表示

$$A = \left[ \begin{matrix} a_1 & \cdots & a_{j-1} & x & a_{j+1} & \cdots & a_n \end{matrix} \right]$$

定义一个变换T为$T(x) = det \left[ \begin{matrix} a_1 & \cdots & a_{j-1} & x & a_{j+1} & \cdots & a_n \end{matrix} \right]$

则：

$$T(cx) = c \cdot T (x)$$

$$T(u+v) = T(u) + T(v)$$

# Part.2 行列式应用 

## 2.1 克拉默法则

令$A_i(\mathbf{b})$表示矩阵A中第i列被替换为b向量的矩阵

$$A_i(\mathbf{b}) = \left[ \begin{matrix} \mathbf{a}_1 & \cdots & \mathbf{b} & \cdots & \mathbf{a}_n\end{matrix}\right]$$

则有以下等式：

$$x_i = \frac{detA_{i}(\mathbf{b})}{detA}, i=1,2,\cdots, n$$

注意，克拉默法则是一个理论工具，计算很大的矩阵时，计算量反而比行化简增加

### 1) 解方程组

设有方程组：

$$\left\{  \begin{matrix} 3x_1 & - & 2x_2 & = & 6 \\ -5x_1 & + & 4x_2 & = & 8\end{matrix} \right.$$

由克拉默法则：

$$A = \left[ \begin{array}{rr} 3 & -2 \\ -5 & 4\end{array}\right], A_{1}(\mathbf{b})=\left[ \begin{array}{rr} 6 & -2 \\ 8 & 4\end{array}\right], A_{2}(\mathbf{b})=\left[ \begin{array}{rr} 3 & 6 \\ -5 & 8 \end{array}\right]$$

$$\begin{matrix} x_1 & = & \frac{detA_{1}(\mathbf{b})}{detA} & = & \frac{24+16}{2} & =20 \\ x_2 & = & \frac{detA_{2}(\mathbf{b})}{detA} & = & \frac{24+30}{2} & =27\end{matrix}$$

### 2) 解线性微分方程

当方程组的系数含有参数时：

$$\left\{  \begin{matrix} 3sx_1 & - & 2x_2 & = & 4 \\ -6x_1 & + & sx_2 & = & 1\end{matrix} \right.$$

由克拉默法则：

$$A = \left[ \begin{array}{rr} 3s & -2 \\ -6 & s\end{array}\right], A_{1}(\mathbf{b})=\left[ \begin{array}{rr} 4 & -2 \\ 1 & s\end{array}\right], A_{2}(\mathbf{b})=\left[ \begin{array}{rr} 3s & 4 \\ -6 & 1 \end{array}\right]$$

由于$detA = 3s^2-12=3(s+2)(s-2)$, 当且仅当$s \neq \pm2$时，方程组有唯一解：

$$\begin{matrix} x_1 & = & \frac{detA_{1}(\mathbf{b})}{detA} & = & \frac{4s+2}{3(s+2)(s-2)} \\ x_2 & = & \frac{detA_{2}(\mathbf{b})}{detA} & = & \frac{3s+24}{3(s+2)(s-2)}\end{matrix}$$

### 3) 求矩阵的逆

设A是一个可逆方阵，$A^{-1}=\frac{1}{detA}adjA$

其中，adjA为`伴随矩阵`，里面的元素是`余因子式`组成的, 但是它是余因子矩阵的**转置(行变列)**， 第一行第二列余因子，对应adjA的第二行第一列：

$$adjA = \left[ \begin{matrix} C_{11} & C_{21} & \cdots & C_{n1} \\ C_{12} & C_{22} & \cdots & C_{n2} \\ \vdots & \vdots & & \vdots \\ C_{1n} & C_{2n} & \cdots & C_{nn} \\\end{matrix}\right]$$

## 2.2 计算面积和体积

### 1) 面积与体积计算

`定理9`：对于2x2矩阵，$|detA|$表示列确定的平行四边形的面积，对于3x3矩阵，$|detA|$表示列确定的平行六面体的体积

证明：[0, a] 和 [b, 0] 构成的矩形面积为$a \times b$

### 2) 线性变换后的面积与体积

设T是一个线性变换，把矩阵A变成了矩阵B，则变换后的面积或体积为：

$$Volumn B = |det T | \cdot |detA|$$