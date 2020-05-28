[TOC]

---

![](https://cdn.jsdelivr.net/gh/HowcanoeWang/HowcanoeWang.github.io/blog/files/19/01线性方程组.svg)

# Part.1 基本问题

## (1) 线性方程组&解集定义

|定义|描述|
|---|---|
|线性方程|形如$$a_1 \cdot x_1 + a_2 \cdot x_2 + \cdots + a_n \cdot x_n = b$$的方程|
|系数|$$a_1, a_2, \cdots, a_n$$|
|线性|自变量$$x_i$$都为一次，$$x_1 \cdot x_2$$和$$\sqrt{x_i}$$都不是|
|线性方程组|由几个包含相同变量$$x_1, x_2, \cdots, x_n$$的`线性方程`组成的, $$\left\{ \begin{array} 2x_1 & -x_2 & 1.5x_3 & = & 8 \\ x_1 & & -4x_3 & = & -7 \end{array} \right.$$|
|线性方程的**解**|一组数$$(s_1, s_2, \cdots, s_n)$$, 用这组数分别代替$$x_i$$,方程变为等式|
|线性方程组的**解集**|一组数同上使方程组变为等式组|
|方程组**等价**|具有相同的`解集`|
|方程组**相容**|有解(1个或多个)|
|方程组**不相容**|无解|
|线性方程组两个基本问题|1. `存在性` $$\rightarrow$$ 是否有解<br>2. `唯一性` $$\rightarrow$$ 是否只有唯一解|



## (2) 矩阵表示


|定义|描述|
|---|---|
|系数矩阵|把每一个变量的系数写在对其的一列$$ \left\{ \begin{array}{rrrcr} x_1 & -2x_2 & +x_3 & = & 0 \\ & 2x_2 & -8x_3 & = & 8 \\5x_1 & & -5x_3 & = & 10 \end{array}\right. \rightarrow \left[ \begin{array}{rrr} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5 \end{array}\right] $$|
|增广矩阵|把右边常数列也添加上$$ \left\{ \begin{array}{rrrcr} x_1 & -2x_2 & +x_3 & = & 0 \\ & 2x_2 & -8x_3 & = & 8 \\5x_1 & & -5x_3 & = & 10 \end{array} \right. \rightarrow \left[ \begin{array}{rrr\|r} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{array} \right] $$|
|初等行变换(行化简)|1. **倍加变换**: 某一行换成该行和另一行的和<br>2. **对换变换**: 把两行交换<br>3. **倍乘变换**: 把某一行所有值同时乘非零值|
|行等价|某个矩阵可以经过`初等行变换`变为另一个矩阵 $$\rightarrow$$ 他俩具有相同的解集|



上接**Part.4 矩阵方程Ax=b**

## (3) 线性方程组的解集（书1.5节）

| 定义                                 | 描述                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| 齐次 / 非齐次                        | 当矩阵方程$A\mathbf{x}=\mathbf{b}$中, $\mathbf{b}$为$\mathbf{0}$, 即方程组的右边一列都是0, 则称为`齐次`的 |
| 平凡解                               | $\mathbf{x}=\mathbf{0}$是必然存在的(`零向量`几何意义为坐标轴`原点`) |
| 非平凡解                             | 其他不为0的"份数"组合, 使得"合力"为0 (把A中每列视为一个方向的力, `解集`为对应力的**份数**)<br />当且仅当方程至少有一个`自由变量`,齐次(矩阵)方程$A\mathbf{x}=\mathbf{b}$有非平凡解 |
| 向量形式                             | 描述$10x_1-3x_2-2x_3=0$ (1) 的`解集`时, 化简为$x_1=0.3x_2+0.2x_3$, 其中$x_2$和$x_3$为`自由变量`,  通解为<br>$$\mathbf{x} = \left[ \begin{matrix} x_1 \\ x_2 \\ x_3 \end{matrix}\right] = \left[ \begin{matrix} 0.3x_2+0.2x_3 \\ x_2 \\ x_3 \end{matrix}\right] = \left[ \begin{matrix} 0.3x_2 \\ x_2 \\ 0 \end{matrix}\right] + \left[ \begin{matrix} 0.2x_3 \\ 0 \\ x_3 \end{matrix}\right] = x_2\left[ \begin{matrix} 0.3 \\ 1 \\ 0 \end{matrix}\right] + x_3 \left[ \begin{matrix} 0.2 \\ 0 \\ 1 \end{matrix}\right]$$ <br>即化为$\mathbf{x}=x_2 \cdot \mathbf{u} + x_3 \cdot \mathbf{v}$ (2) |
| 向量形式的几何意义                   | 上面一条, 表明(1)的每个解都是(2)式表示的向量$\mathbf{u}$和$\mathbf{v}$的`线性组合`, 由于两个向量不重叠, 所以`解集`是通过向量$\mathbf{u}$和$\mathbf{v}$的平面$=span\{\mathbf{u}, \mathbf{v}\}$ |
| 把方程组解集改成参数向量形式         | 1. 把`增广矩阵`行化简成`简化阶梯型`<br />2. 把每个基本变量用自由变量表示<br />3. 把解$\mathbf{x}$表示成向量, 如果有自由变量, 其元素依赖于自由变量<br />4. 把$\mathbf{x}$分解成向量(元素为常数)的`线性组合`, 用`自由变量`作为`参数` |
| 参数向量方程                         | 上面`向量形式`(1)是平面的`隐式`描述(解析几何), 解方程就是找到这个平面的`显示`描述(用单位向量的分解来表示), 即上面的(2)式$\mathbf{x}=s\mathbf{u}+t\mathbf{v}$(s,t为实数) |
| 非齐次方程组的解                     | $$A=\left[ \begin{array}{rrr} 3 & 5 & -4 \\ -3 & -2 & 4 \\ 6 & 1 & -8\end{array}\right], \mathbf{b}=\left[ \begin{array}{r} 7 \\ -1 \\ -4 \end{array} \right]$$, 解出来$\begin{array}{rrccr} x_1 & & -\frac{4}{3}x_3 & = & -1 \\ & x_2 & & = & 2 \\ & & 0 & = & 0\end{array}$<br />继续化简<br />$$\mathbf{x} = \left[ \begin{matrix} x_1 \\ x_2 \\ x_3 \end{matrix}\right] = \left[ \begin{matrix} -1 + \frac{4}{3}x_3 \\ 2 \\ x_3 \end{matrix}\right] = \left[ \begin{array}{r} -1 \\ 2 \\ 0 \end{array}\right] + \left[ \begin{matrix} \frac{4}{3}x_3 \\ 0 \\ x_3 \end{matrix}\right] = \left[ \begin{array}{r} -1 \\ 2 \\ 0 \end{array}\right] + x_3 \left[ \begin{matrix} \frac{4}{3} \\ 0 \\ 1 \end{matrix}\right]$$<br />得到参数方程$\mathbf{x}=\mathbf{p} + t\mathbf{v}$ (3), p本身也是方程Ax=b的`特解`<br />![平移](https://i.loli.net/2020/05/27/ZX4xRzWigEJmTK5.png) |
| **定理六**：非齐次方程组解的几何解释 | 设方程$A\mathbf{x}=\mathbf{b}$对某个$\mathbf{b}$`相容`(有解), $\mathbf{p}$是一个特解, 则$A\mathbf{x}=\mathbf{b}$的可以由$A\mathbf{x}=\mathbf{0}$的解集平移向量$\mathbf{p}$得到 |



# Part.2 增广矩阵


|定义|描述|
|---|---|
|先导元素|非零行中最左边的非零元素，下面用$$\blacksquare$$表示|
|阶梯型|$$\left[ \begin{matrix} \blacksquare & \ast & \ast & \ast \\ 0 & \blacksquare & \ast & \ast \\ 0 & 0 & 0 & 0\end{matrix} \right] $$1. 非零行都在零行上面<br>2. 下面一行的`先导元素`在上一个`先导元素`右面<br>3. 先导元素所在列下面都是0|
|简化阶梯型(REF、RREF)|$$\left[ \begin{matrix} 1 & 0 & \ast & \ast \\ 0 & 1 & \ast & \ast \\ 0 & 0 & 0 & 0\end{matrix} \right] $$除了上面3点,还有:<br>1. 先导元素值为1<br>2. 先导元素是该列唯一非零元素|
|**定理一**:简化阶梯型唯一性|每个矩阵行等价于唯一一个简化阶梯型矩阵|
|主元位置|矩阵对应的`阶梯型`中先导元素的位置|
|主元列|矩阵中含有`主元位置`的列|
|行化简算法|---------向前步骤---------<br>1. 从最左的非零列开始<br>2. 选一个非零元素作为主元，换行使它到首行<br>3. 用倍加法，把该元素下面都变成0<br>4. 进入下一列，重复上面步骤<br>---------向后步骤---------<br>5. 由最右边的主元开始，把每个主元上方的元素都变换成0<br>6. 该主元变换成1|
|基本变量|把`增广矩阵`变成对应的线性方程组时<br>$$\left[ \begin{array}{rrrr} 1 & 0 & -5 & 1\\ 0 & 1 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{array} \right] \rightarrow  \left\{ \begin{array}{rrrcr} x_1 &  & -5x_3 & = & 1 \\ & x_2 & +x_3 & = & 4 \\ & & 0 & = & 0 \end{array} \right. $$<br>对应主元列的变量$$x_1, x_2$$|
|自由变量|其他没有系数的变量如$$x_3$$等|
|通解+参数表示|把基本变量用自由变量表示，形如<br />$$\left\{ \begin{array}{l} x_1 = 1+5x_3\\ x_2 = 4-x_3 \\ x_3 \text{是自由变量} \end{array}\right.$$<br />的式子，因为$$x_3$$取不同值会影响其他值的取值，<br />这样表示可以表达出所有的取值|
|**定理二**:存在与唯一性定理|增广矩阵最右列不是主元列，即不存在$$\left[ \begin{matrix} 0 & \cdots & 0 & b \end{matrix}\right], b \neq 0$$，<br>则线性方程组`相容`(`存在性`), <br />若没有`自由变量`则有唯一解(`唯一性`)，否则有无穷多解|
|行化简解线性方程组|1. 改成`增广矩阵`<br>2. 化为`阶梯型`，判断是否`相容`(有解)<br>3. (若`相容`)化简成`简化阶梯型`<br>4. 写出简化阶梯型的方程组<br>5. 表示成`通解`与`参数形式`|



# Part.3 向量方程

## (1) 向量

|定义|描述|
|---|---|
|(列)向量|仅含有一列的矩阵，如$$\mathbf{w} = \left[ \begin{matrix} w_1 \\ w_2 \end{matrix} \right]$$，<br/>书中为了省空间，使用了$$(w_1, w_2)$$的形式，注意是**圆括号**|
|$$\mathbb{R}^n$$|$$\mathbb{R}$$表示向量中元素是实数，指数n表示包含n个元素(有n行)|
|零向量|所有元素都为0的向量，元素个数通过上下文确定|
|标量乘法<br>(数乘)|给定向量$$\mathbf{u}$$和实数$$c$$, 把$$\mathbf{u}$$的每个元素乘以$$c$$, 记为$$c\cdot\mathbf{u}$$|
|平行四边形法则|两个向量用平面上的点表示，则他们的和可以用两个向量和0向量为三个顶点的平行四边形第四个顶点<br>![](http://www.ivy-end.com/wp-content/uploads/2013/08/5-1-300x263.png)|
|$$\mathbb{R}^n$$中向量的代数性质|交换律、结合律、分配律<br>1. $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$<br />2. $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$<br />3. $\mathbf{u} + \mathbf{0} = \mathbf{0} + \mathbf{u} = \mathbf{u}$<br />4. $\mathbf{u} + (-\mathbf{u}) = -\mathbf{u} + \mathbf{u} = \mathbf{0}$<br />5. $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$<br />6. $(c+d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$<br />7. $c(d\mathbf{u}) = (cd)\mathbf{u}$<br />8. $1\mathbf{u} = \mathbf{u}$|

## (2) 线性组合
|定义|描述|
|---|---|
|线性组合|给定$$\mathbb{R}^n$$中的向量$$\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_n$$和标量$$c_1, c_2, \cdots, c_n$$, 向量$$\mathbf{y} = c_1\mathbf{v}_1 + \cdots + c_p\mathbf{v}_p$$称为向量v以标量c为`权`的`线性组合`, 几何描述为以这几个向量作为单位坐标网格, 改网格线上对应的点的位置<br>![](https://pic4.zhimg.com/v2-f05fd33a67d91da8d3449b2d6bc10533_r.jpg)|
|向量方程|$$x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n= \mathbf{b}$$<br>设$$\mathbf{a}_1 = \left[ \begin{array}{r} 1 \\ -2 \\ -5 \end{array} \right], \mathbf{a}_2 = \left[ \begin{array}{r} 2 \\ 5 \\ 6 \end{array} \right], \mathbf{b} = \left[ \begin{array}{r} 7 \\ 4 \\ -3 \end{array} \right]$$,  $$\mathbf{b}$$能否写成$$\mathbf{a}_1, \mathbf{a}_2$$的线性组合? 设权$$x_1$$,$$x_2$$, 使得$$x_1\mathbf{a}_1 + x_2\mathbf{a}_2 = \mathbf{b}$$成立, 即解线性方程组$$\left\{ \begin{array}{rrr} x_1 & + 2x_2  & = & 7 \\ -2x_1 & +5x_2 & = & 4 \\ -5x_1 & +6x_2 & = & -3\end{array} \right.$$|
|$$Span\{\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_p\}$$|$$\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_p$$是$$\mathbb{R}^n$$中的向量，他们的所有线性组合所组成的集合(即上图中蓝色坐标能取到的所有点)，专业术语，$$\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_p$$所张成的$$\mathbb{R}^n$$的子集|
|判断$$\mathbf{b}$$是否属于$$Span\{\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_p\}$$|即b能否写成$$\mathbf{v}_1, \mathbf{v}_2, \cdots, \mathbf{v}_p$$的线性组合？即判断向量方程$$x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n= \mathbf{b}$$是否有解，即判断增广矩阵为$$\left[\begin{matrix} \mathbf{v}_1 & \mathbf{v}_2 & \cdots & \mathbf{v}_n & b \end{matrix} \right]$$的线性方程组是否有解|
|$$Span\{\mathbf{u}\}$$和$$Span\{\mathbf{u}，\mathbf{v} \}$$的几何解释$$^{[1]}$$|u、v非0向量，不是互相的倍数(不然就线性相关了)![span{u}+span{u,v}几何解释](https://i.loli.net/2020/05/20/eD3RpCj75PlwGEg.jpg)|



## (3) 线性无关 (书1.7节)

| 定义               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| 线性无关           | 对于给定的向量集$\{\mathbf{v_1}, \cdots, \mathbf{v_n}\}$, 若它构成的`向量方程`<br />$x_1\mathbf{v_1}+x_2\mathbf{v_2}+ \cdots + x_n\mathbf{v_n} = \mathbf{0}$仅有平凡解, <br />即所有$x_i$都为0时, 等式才成立, 则这个向量集`线性无关` |
| 线性相关           | 上面的例子中, 存在**不全为**0的权$x_i$使得等式也成立, 则这个向量集`线性相关` |
| 线性无关的确定方法 | 把对应的`增广矩阵`进行`行变换`, 看是否有`自由变量`, <br />根据`定理二`就是确定是否有系数全是0的行 |
| 矩阵的线性无关     | 矩阵$A=[\mathbf{a_1} \cdots \mathbf{a_n} ]$, 对应的矩阵方程$A\mathbf{x}=\mathbf{0}$可以写成<br />$$x_1\mathbf{a_1}+x_2\mathbf{a_2}+ \cdots + x_n\mathbf{a_n} = \mathbf{0}$$, <br />根据上面的定义, 当它仅有平凡解时, 矩阵A各列线性无关 |
| 几何意义           | 当用上面的**向量集**中的向量(**作为基底**)去构建(变换)成新的坐标系时, <br />如果其中有一个向量, 可以被其他向量表示出来, 那么说明这个向量可以被**省略**(**化简**)掉, 这种情况叫做`线性相关`, <br />当没有任何向量可以被其他向量表示时, 说明这个向量集已经达到了最简的情况, 没法继续化简了, 则这种情况叫做`线性无关` |
| 一个向量的集合     | 当只有一个向量时, 除了向量为0向量, 否则没法用第二个向量来表示, 即任何时候都线性无关 |
| 两个向量的集合     | 当一个向量是另一个向量的倍数时, 符合线性相关的定义, 可以被化简, 即为`线性相关`, 否则`线性无关`<br />![test.png](https://i.loli.net/2020/05/28/gIsCT4BvN1hHJwS.png) |



# Part.4 矩阵方程

| 定义                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 矩阵与向量的积Ax                                             | $$A\mathbf{x}=[\begin{matrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{matrix}] \left[\begin{matrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{matrix}\right]=x_1\mathbf{a}_1+ x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n$$<br>A的各**列**以x中对应元素为**权**的线性组合, 即**线性组合**=矩阵$$\times$$方程 |
| 矩阵方程                                                     | 形式为$$A\mathbf{x}=\mathbf{b}$$的 矩阵$$\times$$权向量=向量 |
| **定理三**:线性方程组的三种等价形式                          | 1. 矩阵方程 $$A\mathbf{x}=\mathbf{b}$$<br>2. 向量方程 $$x_1\mathbf{a}_1+ x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n=\mathbf{b}$$<br>3. 增广矩阵 $$\left[ \begin{matrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n & \mathbf{b} \end{matrix}\right]$$<br>当构造实际生活中的数学模型时, 可以选取任何一种最自然的观点, 也可以从一个观点转换到另一个观点, 求解时都用`增广矩阵行化简`来求 |
| 判断方程$$A\mathbf{x}=\mathbf{b}$$是否对任意的$$\mathbf{b}$$都有解 | 先转换成增广矩阵$$\left[ \begin{matrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n & \mathbf{b} \end{matrix}\right]$$, 然后`行化简`成`阶梯型`,判断增广矩阵是否`相容`, 即通过`定理二`判断是否存在$$\left[ \begin{matrix} 0 & \cdots & 0 & b \end{matrix}\right]$$的行, 没有就适用于所有情况 |
| **定理四**:等价形式的延伸结论                                | 当A为线性方程组的`系数矩阵`时<br>* 方程$$A\mathbf{x}=\mathbf{b}$$对$$\mathbb{R}^m$$中每个$$\mathbf{b}$$都有解 (`矩阵方程`视角)<br>* $$\mathbb{R}^m$$中每个$$\mathbf{b}$$, 都是A的列的一个线性组合 (`向量方程`视角, $$\mathbf{b}$$能写成$$\mathbf{a}_1, \mathbf{a}_n$$的线性组合)<br>* A的各列生成$$\mathbb{R}^m$$ (`Span{}`的定义视角)<br>* A在每一行都有一个主元位置 (矩阵方程`定理二`实际操作) |
| Ax的行-向量规则                                              | 若乘积$A\mathbf{x}$有定义, 则$A\mathbf{x}$中第$i$个元素是$A$的第$i$行元素与$x$的相应元素的乘积之和 |
| 单位矩阵$I$                                                  | 矩阵的主对角线上的元素为1, 其他元素为0, 形如:<br>$$\left[ \begin{matrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \right]$$ |
| **定理五**: 矩阵向量积Ax性质                                 | A是$m \times n$矩阵, $\mathbf{u}$和$\mathbf{v}$是$\mathbb{R}^n$中向量, $c$是标量, 则<br />1. $A(\mathbf{u} + \mathbf{v})=A\mathbf{u} + A\mathbf{v}$<br />2. $A(c\mathbf{u})=c(A\mathbf{v})$ |

下承**Part.1 基本问题**.(3) 线性方程组的解集(书1.5节)



# Part.5 线性变换



# Part.6 应用



# 参考资料

[1] 线性代数中的线性方程组_part1 https://blog.csdn.net/wvence/article/details/7849121

