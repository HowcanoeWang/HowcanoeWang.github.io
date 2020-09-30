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

`定理8`: 可逆矩阵定理

1. A是$n \times n$可逆矩阵

2. A行等价于$n \times n$单位矩阵$I$

    > ($I$可以通过行变换变成A)
   
3. A有n个`主元位置`

4. 方程$A\mathbf{x}=0$仅有平凡解
   
    > x=0, 仅有0解

5. A的各列线性无关

6. 线性变换$x \rightarrow Ax$是一对一的, 且把$\mathbb{R}^n$映射到$\mathbb{R}^n$

7. 对$\mathbb{R}^n$中任意的$\mathbf{b}$, 方程$A\mathbf{x}=\mathbf{b}$至少有一个解

8. A的各列生成$\mathbb{R}^n$

9. 存在$n \times n$矩阵C与D, 使$AC=I$或$AD=I$成立

10. $A^T$依然是可逆矩阵

本节**4.4**之后：

1.  A的列向量构成$\mathbb{R}^n$的一个基
2.  Col A = $\mathbb{R}^n$
3.  dim Col A = n
4.  rank A = n
5.  Nul A = {**0**}
6.  dim Nul A = 0

`定理9`: 有一个线性变换$T$, 如果存在函数S使得对于所有的x值, $S(T(x))=x=T(S(x))$, 那么该线性变换为可逆的

> 并没有看懂

# Part.2 分块矩阵

## 2.1 标量乘法

同样维度的分块可以直接相加

## 2.2 分块乘法

`定理10`:分块矩阵的乘法

$$\begin{array}{lll} AB & = & \left[ \begin{matrix} col_1(A) & \cdots & col_n(A) \end{matrix}\right] \cdot \left[ \begin{matrix} row_1(B) \\ \vdots \\ row_n(B) \end{matrix}\right] \\ & = & col_1(A)row_1(B)+ \cdots + col_n(A)row_n(B) \end{array}$$

## 2.3 分块的逆

`分块上三角矩阵`: 形如$A=\left[ \begin{matrix} A_{11} & A_{12} \\ 0 & A_{22}\end{matrix} \right]$的矩阵

求它的逆可以通过构造新矩阵B, 使得 $AB=\left[ \begin{matrix} A_{11} & A_{12} \\ 0 & A_{22}\end{matrix} \right]\left[ \begin{matrix} B_{11} & B_{12} \\ B_{21} & B_{22}\end{matrix} \right]=\left[ \begin{matrix} I_P & 0 \\ 0 & I_q \end{matrix} \right]$, 从而获取$B$关于A的表达式:

$$A^{-1}=\left[ \begin{matrix} A_{11}^{-1} & - A_{11}^{-1} A_{12} A_{22}^{-1} \\ 0 & A_{22}^{-1}\end{matrix} \right]$$


# Part.3 因式分解

## 3.1 LU分解

可以把$A$分解成$LU$, 按照下面的形式:

$$A=\left[ \begin{matrix} 1 & 0 & 0 & 0\\ \star & 1 & 0 & 0 \\ \star & \star & 1 & 0 \\ \star & \star & \star & 1\end{matrix} \right] \left[ \begin{matrix} \blacksquare & \star  & \star & \star \\ 0 & \blacksquare & \star & \star \\ 0 & 0 & \blacksquare & \star \\ 0 & 0 & 0 & \blacksquare \end{matrix}\right]$$

左边的L是可逆的`下三角矩阵`, 主对角线元素都是1, 右边的U是A的`阶梯型矩阵`.

解方程$A\mathbf{x}=\mathbf{b}$时, 可以先做一个LU分解，变换成$LU\mathbf{x}=\mathbf{b}$ 

令$U\mathbf{x}=\mathbf{y}$, 可以得到$L\mathbf{y}=\mathbf{b}$.

只用非常简单的几步行变换即可算得y：

$$\left[ \begin{matrix} L & \mathbf{b} \end{matrix}\right] = \left[ \begin{array}{cccc|c} 1 & 0 & 0 & 0 & b_1 \\ \star & 1 & 0 & 0 & b_2 \\ \star & \star & 1 & 0 & b_3 \\ \star & \star & \star & 1 & b_4 \end{array} \right] \sim \left[ \begin{array}{cccc|c} 1 & 0 & 0 & 0 & y_1 \\ 0 & 1 & 0 & 0 & y_2 \\ 0 & 0 & 1 & 0 & y_3 \\ 0 & 0 & 0 & 1 & y_4\end{array} \right] = \left[ \begin{matrix} I & \mathbf{y} \end{matrix}\right]$$

知道了y，再去求解x, 也是非常简单的行变换：

$$\left[ \begin{matrix} U & \mathbf{y} \end{matrix}\right] = \left[ \begin{array}{cccc|c} \blacksquare &  \star & \star & \star & y_1 \\ 0 & \blacksquare & \star & \star & y_2 \\ 0 & 0 & \blacksquare & \star & y_3 \\ 0 & 0 & 0 & \blacksquare & y_4 \end{array}\right] \sim \left[ \begin{array}{cccc|c} 1 & 0 & 0 & 0 & y_1 \\ 0 & 1 & 0 & 0 & y_2 \\ 0 & 0  & 1 & 0 & y_3 \\ 0 & 0 & 0 & 1 & y_4 \end{array}\right] = \left[ \begin{matrix} I & \mathbf{x} \end{matrix} \right]$$

因此先做LU分解可以大幅减少解方程的计算量

## 3.2 分解算法

1. 对原始矩阵 A进行行化简，得到U
2. 对于上面过程中的每一步，把行化简前的主元列单独拎出来，采下三角的部分，然后想着这一列，怎么倍乘变换才能把对角线变成1，这一列的数字就除以这个倍数，获得1开头的所有主元列，组装起来就是L

# Part.4 属性

## 4.1 子空间

`子空间`是一个$\mathbb{R}^n$中的一个集合H，且满足以下条件：

1.  零向量属于H（**过原点**，非常重要，例2就举了一个反例）
2.  对于H中的任意向量，u+v也属于H (类似于平行四边型法则)
3.  对于H中的任意向量，u的常数c倍也属于H (向量的延长)

或者说，$Span\{v_1, \cdots, v_p\}$是由$v_1, \cdots, v_p$所张成的子空间

PS：$\mathbb{R}^n$是他自身的子空间，仅包含零向量的子空间也是特殊的子空间，叫`零子空间`

`列空间`：矩阵A的各列的`线性组合`的集合, 即$A=[a_1 \cdots a_n]$, $Span\{a_1, \cdots, a_n\}$就是列空间，记为Col A

判断一个向量b是否属于一个列空间Col A，就是判断方程Ax=b是否`相容`(有解)

`零空间`：齐次方程Ax=0的所有解的集合，记为Nul A，同时也具有$\mathbb{R}^n$子空间的性质

`定理12`：$m \times n$的矩阵A的零空间是$\mathbb{R}^n$的子空间，等价于，n个未知数的m个齐次线性方程组Ax=0的所有解的集合也是$\mathbb{R}^n$的子空间

子空间的`基`：子空间H中一组线性无关集，生成H， 如(0,1)和(1,0)，或(1,0,0), (0,1,0)和(0,0,1), 就是`标准基`, 即$\{e_1, \cdots, e_n\}$每列都为1

`列6`：解方程Ax=0的参数向量形式，就是确定Nul A的`基`

`列7`->`定理13`：矩阵B的主元列，就是Col B的`基`, 因为其他列可以被主元列表示出来

## 4.2 坐标系

设`子空间`H内有一组基$B=\{\mathbf{b}_1, \cdots, \mathbf{b}_p\}$, 对于某个向量$x$，用这组基来表示的`权`，即$x = c_1 \mathbf{b}_1 + \cdots + c_p \mathbf{b}_p$ 成立时，称为`x(相对于B)的坐标向量`，记作$[\mathbf{x}]_B = \left[ \begin{matrix} c_1 \\ \vdots \\ c_p \end{matrix} \right]$

## 4.3 维数

`维数`(dim H)：是任意一个基的**向量个数**，一个经过原点的线dim=1，一个经过原点的平面dim=2，$\mathbb{R}^n$的维数为n

零空间的维数(dim Nul A), 由于求Nul A就是就Ax=0的参数向量形式，而向量个数由`自由变量`决定，所以dim Nul A=自由变量的个数

## 4.4 秩

矩阵A的`秩`(rank A)：是A列空间的`维数`(rank A = dim col A)，由于`主元列`构成Col A的一个基，所以rank A就是A的主元列的个数

`定理14`(秩定理)：如果一矩阵A有n列，则rank A = dim Nul A

`定理15`(基定理)：$\mathbb{R}^n$的p维子空间H(**如3维的中的一个过原点平面H**)，H中任何由p个非线性相关的元素构成H的一个基(**平面中任何2个非线性相关向量构成平面的基**)，并且

> H中任何生成H的p个向量集也构成H的一个基(**啥意思？**)


# Part.5 应用
## 5.1 电子网络电压电流

一个电路的输入端和输出端的电压和电流可以表示为$\left[ \begin{matrix} v_1 \\ i_1\end{matrix} \right]$和$\left[ \begin{matrix} v_2 \\ i_2 \end{matrix} \right]$,然后可以定义这个电路为一个线性变换矩阵(`传递矩阵`)A，使得$\left[ \begin{matrix} v_2 \\ i_2 \end{matrix} \right] = A \left[ \begin{matrix} v_1 \\ i_1 \end{matrix} \right]$成立。

那么在一个`梯级网络`中, 即有很多上面的单位电路组成的串联电路(第一个电路的输出是第二个电路的输入)，已知串联电路和并联电路的`传递矩阵`与电阻R的关系如下：

*   串联电路: $\left[ \begin{array}{rr} 1 & -R_1 \\ 0 & 1 \end{array} \right]$
*   并联电路: $\left[ \begin{array}{cc} 1 & 0 \\ -1 / R_2 & 1 \end{array} \right]$

![image.png](https://i.loli.net/2020/07/15/MocEZjBt9dOLFRy.png)

那么上面的这个电路就可以看为, $\mathbf{x}$先经过$A_1$左边传递矩阵的变换为$A_1\mathbf{x}$, 然后再经过$A_2$右边的传递矩阵变为$A_2(A_1\mathbf{x})$, 则

$$A_2A_1 =\left[ \begin{array}{cc} 1 & 0 \\ -1 / R_2 & 1 \end{array} \right] \left[ \begin{array}{rr} 1 & -R_1 \\ 0 & 1 \end{array} \right] = \left[ \begin{array}{cc} 1 & -R_1 \\ -1 / R_2 & 1 + R_1/ R_2 \end{array} \right]$$

## 5.2 列昂惕夫投入产出模型

经济体中,除了像第一章的投入产出模型, 每个生产部门都消耗其他生产部门的产出以外, 这一章又增加了一个`开放部门`, 没有生产只有消费别人的产出. 除此之外, 有一个向量$\mathbf{d}$叫做最终需求向量, 为一通操作之后, 还剩下的产品.

$$\text{总产出} x = \text{中间需求} Cx + \text{最终需求} d$$

C为投入产出矩阵(`消耗矩阵`): 

| (购买自) | 制造业 | 农业 | 服务业 |
| -------- | ------ | ---- | ------ |
| 制造业   | 0.50   | 0.40 | 0.20   |
| 农业     | 0.20   | 0.30 | 0.10   |
| 服务业   | 0.10   | 0.10 | 0.30   |

则有 $C=\left[ \begin{matrix} 0.50 & 0.40 & 0.20 \\ 0.20 & 0.30 & 0.10 \\ 0.10 & 0.10 & 0.30 \end{matrix} \right]$

为了求最终需求, 可以化简上面的公式:

$$d = (I-C)x$$

或者(`定理11`: C为消耗矩阵, d为最终需求, 若C和d的元素非负, C的每一列和小于1, 则$(I - C)^{-1}$存在且产出向量x有唯一解)

$$x = (I - C)^{-1} d$$

## 5.3 计算机图形学应用

### 1) 齐次坐标

在平面上面平移， 并不能用矩阵乘法表示出来，因为平移不是线性变换，为了解决这一困难，特地引进

`齐次坐标`: 在$\mathbb{R}^2$中的一个点$(x, y)$, 可以用对应$\mathbb{R}^3$中的点$(x, y, 1)$来表示， 但是不可以加或乘以常数，只能用于$3 \times 3$的矩阵变换

$(x, y) \rightarrow (x+h, y+k)$可以用齐次坐标实现$\left[ \begin{matrix} 1 & 0 & h \\ 0 & 1 & k \\ 0 & 0 & 1\end{matrix}\right] \left[ \begin{matrix} x\\ y \\ 1\end{matrix}\right] = \left[ \begin{matrix} x + h\\ y + k \\ 1\end{matrix}\right]$

### 2) 复合变换

当需要多个基本变换叠加使用时，可以用矩阵乘法来算出最终的变换矩阵。但是这边要注意，先变换的要写在右边，每次都是左乘，即$A_n A_{n-1} \cdots A_1$,然后计算的时候，从左往右依次计算

### 3) 齐次三维坐标

一般称$\mathbb{R}^3$中的点$(x, y, z)$的齐次坐标为$(x, y, z, 1)$或$(X,Y,Z,H)$且$x=\frac{X}{H}, y=\frac{Y}{H}, z=\frac{Z}{H}$， 如果希望把$(x, y, z)$变换到$(x+h, y+k, z+j, 1)$，则变换矩阵为

$$\left[ \begin{matrix} 1 & 0 & 0 & h \\ 0 & 1 & 0 & k \\ 0 & 0 & 1 & j \\ 0 & 0 & 0 & 1\end{matrix}\right]$$

**注意1**：和平面齐次坐标一样，坐上的单位矩阵$I$可以替换为任何线性变换，表示先进行其他的变换处理。

**注意2**：如果算出来的齐次坐标，最后一位不为1，则需要把最后一位变换成1才可以作为最终的转换后坐标(投影变换例8)。

### 4) 投影变换

在一个平面直角坐标系里面，沿着Z轴的垂直投影，眼睛的位置在d，三维空间中有一点$(x, y, z)$，求投到XY平面上面的坐标是什么

![image.png](https://i.loli.net/2020/07/21/i59XfqNhpKJuPek.png)

根据三角形相似，可以解得

$$\begin{array}{l} x^{\star} = \frac{dx}{d-z} = \frac{x}{1-z/d} \\ y^{\star} = \frac{y}{1-z/d} \end{array}$$

因此，透视投影的参数方程为$(\frac{x}{1-z/d}, \frac{y}{1-z/d}, 0, 1)$, 也可表示为$(x, y, 0, 1-z/d)$,从而得到投影变换矩阵为

$$\left[ \begin{matrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & -1/d & 1\end{matrix}\right] \left[ \begin{matrix} x \\ y \\ z \\ 1\end{matrix}\right] = \left[ \begin{matrix} x \\ y \\ 0 \\ 1 - z/d \end{matrix}\right]$$

**注意**，当应用上面的公式对三维坐标进行变换后，如果第四维参数不为1， 则需要先归一化之后，才可以取前面的2维作为投影后的二维坐标 

