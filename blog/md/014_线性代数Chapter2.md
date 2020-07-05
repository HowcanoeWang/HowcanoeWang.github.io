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

A的维度为$m \times n$, 则$A^T$的维度为$n \times m$

$$B = \left[ \begin{array}{rr} -5 & 2 \\ 1 & -3 \\ 0 & 4\end{array}\right], B^T = \left[ \begin{array}{rrr} -5 & 1 & 0 \\ 2 & -3 & 4\end{array}\right]$$

`定理3`: 设A与B表示矩阵, 其`维数`使得等式成立, r为实数:

1.  $(A^T)^T = A$
2.  $(A+B)^T = A^T + B^T$
3.  $(rA)^T = rA^T$
4.  $(AB)^T=B^T A^T$

## 1.3 逆

`可逆的`：有一个$n \times n$矩阵A，如果存在一个$n \times n$矩阵C，使得$AC = I$且$CA=I$都成立

### 1) 奇异矩阵

`不可逆矩阵`：也被称为`奇异矩阵`

`可逆矩阵`：也成为`非奇异矩阵`

### 2) 行列式

对于一个$2 \times 2$矩阵$A=\left[ \begin{matrix} a & b \\ c & d\end{matrix} \right]$

`行列式`：$detA = ad - bc$

`定理4`：若$detA \neq 0$, 则$A$`可逆`且$$A^{-1}=\frac{1}{ad-bc} \left[ \begin{array}{rr} d & -b \\ -c & a\end{array} \right]$$

`定理5`：若A是可逆矩阵，则对符合维度($\mathbb{R}^n$)中的$\mathbf{b}$， 方程$Ax=\mathbf{b}$有唯一解$x=A^{-1}\mathbf{b}$ (两式同时左乘$ A^{-1}$)

>   可用上面的思想来解方程组，先求出来逆矩阵，然后直接相乘，但是计算机里面很少用，因为复杂度比行化简要大

`定理6`：可逆矩阵的三个有用事实

1.  若A是可逆矩阵，则$A^{-1}$也可逆，即$(A^{-1})^{-1}=A$
2.  若A和B都是$n \times n$可逆矩阵，则AB也可逆，且AB的逆是A和B的逆矩阵相反顺序的乘积, 说人话：$(AB)^{-1}=B^{-1}A^{-1}$
3.  若A可逆，则$A^T$也可逆，且$(A^T)^{-1}=(A^{-1})^T$

### 3) 初等矩阵E

`初等矩阵`：把单位矩阵进行**一次**初等行变换，就能得到**初等矩阵**，如下面三种：

1.  倍加变换：$E_1=\left[ \begin{matrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 4 & 0 & 1\end{matrix} \right]$
2.  对换变换：$E_2=\left[ \begin{matrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1\end{matrix} \right]$
3.  倍乘变换：$E_3=\left[ \begin{matrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 5\end{matrix} \right]$

`定理7`：矩阵A是可逆的，把$A$化简为$I_n$的行变换步骤，同时也可以把$I_n$变换成$A^{-1}$

### 4) 逆矩阵计算算法

根据`定理4`，把$A$和$I$排在一起构成新的矩阵$\left[ \begin{matrix} A & I \end{matrix} \right]$, 利用行变换把坐标的$A$变成$I$, 即行等价于$\left[ \begin{matrix} I & A^{-1} \end{matrix} \right]$, 右边的就是要的矩阵的逆

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



