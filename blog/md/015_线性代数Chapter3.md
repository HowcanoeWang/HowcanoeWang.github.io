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

### 1) 解方程组

### 2) 解线性微分方程

### 3) 求矩阵的逆

## 2.2 计算面积和体积

### 1) 面积计算

### 2) 体积计算

### 3) 线性变换后的面积与体积

