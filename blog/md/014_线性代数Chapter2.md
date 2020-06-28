[toc]

---
![](https://cdn.jsdelivr.net/gh/HowcanoeWang/HowcanoeWang.github.io/blog/files/14/02矩阵代数.svg)

# Part.1 矩阵运算

## 1.1 乘法

`对角矩阵`：一个方阵，除了对角线的元素都为0
`零矩阵`: 所有的元素都为0，维度根据上下文确定

### 1) 和与标量乘法

两个矩阵具有同样的维度才可以做以下运算：

`定理1`：设ABC是相同维度的矩阵，r和s为常数，则有

1.  $A + B=B + A$
2.  $(A+B)+C = A + (B+C)$
3.  $A+0 = A$
4.  $r(A+B)=rA+rB$
5.  $(r+s)A=rA+sA$
6.  $r(sA)=(rs)A$

### 2) 矩阵乘法

定义：$A$是$m \times n$矩阵，$B$是$n \times p$矩阵，乘积$AB$是$m \times p$矩阵，即

$$AB=A[\begin{matrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_p \end{matrix}] = [\begin{matrix} A\mathbf{b}_1 & \mathbf{b}_2 & \cdots & A\mathbf{b}_p \end{matrix}]$$

`行列法则`：AB乘积有定义，则AB的第i行第j列的元素是A的第i行和B的第j列的元素乘积的和

![image.png](https://i.loli.net/2020/06/26/Hhv4epALzqyS6FT.png)

`定理2`：设A为$m \times n$矩阵，B和C的`维数`使得乘积有意义，则：

1.  乘法结合律: $A(BC)=(AB)C$
2.  乘法左分配律$A(B+C)=AB+AC$
3.  乘法右分配律$(B+C)A=BA+BC$
4.  $r(AB)=(rA)B=A(rB)$
5.  矩阵乘法的恒等式$I_m A = A = AI_m$
6.  交换律**一般不成立**$AB \neq BA$
7.  消去律**一般不成立**$AB=AC \nrightarrow B=C$
8.  $AB=0$, **不一定**AB有一个必为0矩阵

### 3) 乘幂

$$A^k = A \cdot A \cdots (k\text{个}) \cdots A \cdot A$$

$A^0$为`单位矩阵`

## 1.2 转置

A的维度为$m \times n$, 则$A^T$的维度为$n \times m$, 且

`定理3`: 设A与B表示矩阵, 其`维数`使得等式成立, r为实数:

1.  $(A^T)^T = A$
2.  $(A+B)^T = A^T + B^T$
3.  $(rA)^T = rA^T$
4.  $(AB)^T=B^T A^T$

## 1.3 逆

### 1) 奇异矩阵

### 2) 行列式

### 3) 初等矩阵

### 4) 计算算法

### 5) 可逆矩阵特征(附带书2.8 秩定理)

# Part.2 分块矩阵

## 2.1 标量乘法

## 2.2 分块乘法

## 2.3 分块的逆


# Part.3 因式分解

## 3.1 LU分解

## 3.2 分解算法

# Part.4 属性

## 4.1 子空间

## 4.2 维度

## 4.3 秩


# Part.5 应用
## 5.1 电子网络电压电流

## 5.2 列昂惕夫投入产出模型



## 5.3 计算机图形学应用



