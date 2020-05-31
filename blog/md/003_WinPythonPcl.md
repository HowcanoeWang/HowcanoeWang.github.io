**2020年5月更新**：

2019年，Intel公司发布了新的3D库：**Open3D**，强烈推荐作为python环境下的点云处理主力库（如果对pcl里的功能依赖不大的话；PS：依赖很大还是要老老实实回去学C++，这个Python-PCL提供的接口实在有限）

---

本文主要讲解Python-PCL库的背景知识与搭建步骤，主要内容有：

[toc]

# 背景知识

【说些废话与基础知识，主要是理解，为后面实际操作做准备】

## Python

Python，是一种广泛使用的高级编程语言，她的设计哲学是强调代码的可读性和简洁的语法 (尤其是强制使用空格缩进划分代码块而非大括号或关键词)，她跨平台和开源的特点，使其作为一门胶水语言，被广泛的应用在了各个领域中。

![pythoneer](https://img.moegirl.org/common/c/c0/Python.jpg "Python是世界上最美的语言(痴汉脸)")

## 点云

空间直角坐标系中一系列点的集合即为点云，获取的方式主要为激光雷达扫描和图像立体视觉反算(Structure from Motion, SfM)获得，主要包含空间坐标信息(X,Y,Z)，也可在此基础上，补充颜色(RGB)、反射面强度、分类属性等信息，是一种描述空间信息的有效方式。

![点云图像](https://i.loli.net/2020/04/01/28zgpaBUqk6uNvj.jpg "点云三维可视化展示.jpg")

## PCL库

![PCL-logo](https://i.loli.net/2020/05/24/nXEaDCxM7vehArS.png)

PCL (Point Cloud Libray) 是大型跨平台开源C++编程库，实现了大量点云相关的通用算法和高效数据结构，涉及到点云获取、滤波、分割、配准、特征提取、曲面重建及可视化等功能，PCL在3D信息获取与处理上和OpenCV在2D信息获取上有着同样的地位。其采用BSD证书，可免费进行商业和学术应用。

作为优秀的胶水语言，python-pcl封装了部分PCL库的接口，截至2018年5月，主要包括基于PointXYZ点云类型的5个操作：

* 点云文件的读写操作(I/O)
* 点云分割 (Segmentation)
* 平滑操作 (Smoothing)
* 滤波操作 (Filtering)
* 配准操作 (Registration)

可以说非常基础了，没有完全发挥出来它在C++平台上的威力，不过该python库也在18个贡献者的努力下不断扩建中。

## Python虚拟环境

Python发展至今，版本迭代十分迅速；就算相同的Python版本下，各个库也有不同的版本，对于开发人员来说，解决开发不同应用的版本冲突问题尤为重要，虚拟环境的出现，相当于给每个应用一个单独的房间，互相之间不会影响。

对于笔者来说，Python3.6是最常用(甚至是默认)的一个Python版本，科研数据处理中主要要用到最新版本的Numpy、Matplotlib、Pandas三件套，但是很多种情况下，很多库的开发人员是“御姐控”，更喜欢老版本的成熟稳定，如本文的主角，他就要求Python版本号最好不高于3.5，Cython版本号不得高于0.25.2；这与笔者的科研数据处理需求就起了很严重的版本冲突。

这种独立隔开的房间，一方面可以解决版本冲突问题，另一方面可以保证处女座程序员对开发环境的整洁的需求。像笔者这种各个方向乱捯饬的反面例子，常用的科研数据处理，就安装了10多个库；然后数据展示的Jupyter Notebook这个应用，又安装了几十个库；前不久又跑去学爬虫，又装了近10个爬虫库；Python动态网页开发，又装了一大堆Flask库，导致现在每次一输入`pip list`进行库管理时，列出来乱七八糟的近百行库列表令人头大。如果每个方向专门开一个房间，那可不就清爽多了。

虚拟环境的安装很简单，打开命令控制行(Win+R>输入cmd 或 右键开始菜单的Win图标>选择Windows Powershel 管理员)，输入

```bash
C:\Users\Admin> pip install virtualenv
```

即可

（以下步骤建议在管理员模式中启动，但是这里是基础知识讲解，不是环境搭建的操作，）
创建虚拟环境的主要的操作步骤有：

* 创建目录
* 创建虚拟环境
* 进入虚拟环境
* 安装包
* 推出环境
* 删除环境

### 1.创建目录

```bash
C:\Users\Admin> cd D:\ # 切换到D盘根目录
D:\> mkdir Virtualenv # 新建一个叫Virtualenv的文件夹
D:\> cd Virtualenv # 进入文件夹内
D:\Virtualenv> # 进来了，可以进行下一步了
```

### 2.创建命名为XXX的独立虚拟环境

```bash
virtualenv 虚拟环境名 --python=你要创建的Python版本地址\python.exe --no-site-packages
```

--为可选项，如果--python没给定，就创建系统默认Python版本的虚拟环境，--no-site-packages如果没给定，就默认复制系统默认Python版本的所有库，建议加上，不然和直接安装没太大区别啊。

以下是栗子，成功的建立一个名叫pcl的Python3.5的虚拟环境

```bash
D:\Virtualenv> virtualenv pcl --python=D:\Applications\Python35\python.exe
```

### 3.进入虚拟环境:\Scripts\activate

```bash
D:\Virtualenv> pcl\Scripts\activate
```

然后效果就是

```bash
(pcl) D:\Virtualenv>
```

注意到前面虚拟环境的小括号了没有，这就说明进独立的虚拟环境啦。

### 4.安装各种包

虚拟环境里安装包和普通的操作一模一样，顺便在这里补充一下安装包的3种姿势：

#### 第一种，也是最普遍的

```bash
pip install 包名 --version=版本号
```

Python的基本操作啊，必须要会的，后面特定版本的Cython就是用这种方法（敲黑板）

#### 第二种，进阶了一点，wheel安装法

这种方法主要出现在默认的Pip安装的包有些问题，需要找第三方平台放出来的修改版本，最最常见的就是Intel的CPU基本都有mkl架构，这种情况下默认安装的numpy和scipy不能正常运行，需要安装第三方拓展包啦，网址：https://www.lfd.uci.edu/~gohlke/pythonlibs/

用Intel CPU的小伙伴的numpy+mkl就要用这种方法安装，要不为啥说农企AMD很优秀呢→_→

此外，mkl还要建立在微软C++运行库上面，记得根据自己的Python版本安装对应的版本号：

*   Visual C++ 2008 (x64, x86, and SP1 for CPython 2.7) redistributable packages
*   Visual C++ 2010 (x64, x86, for CPython 3.4) redistributable packages
*   Visual C++ 2017 (x64 or x86 for CPython 3.5, 3.6, and 3.7) redistributable packages

这里要注意，巨硬有个很优秀的设计，就是当新版本存在时，老版本无法安装，所以如果这些版本号都要用到的话，要从老版本先开始装起 (╯‵□′)╯︵┻━┻

下载地址就在上面那个链接里面，点对应的超链接就能下载啦。

安装完了之后，下载对应版本的numpy+mkl.whl文件，然后依然是命令行里面

```bash
pip install 下载地址\numpy+mkl.whl
```

#### 第三种，伪开发人员安装法

这种方法适用于，开发人员既没有在pypi上注册名字(即不能pip install 包名)，也没有打包好的whl轮子文件，但是他的源文件，有个叫setup.py的东西，就要用这个文件来安装。

```bash
python setup.py build_ext -i # 测试可行性，一定要测试通了再进行下一步
python setup.py install # 安装包
```

看，就安装这么一个玩意，pip安装包的3个主要考点全都涵盖了，很优秀的经典例题啊，放高考里那可是必考的。

### 5.退出当前虚拟环境

捯饬完了之后，就可以退出虚拟环境了，方法很简单，直接输入deactivate即可。

```bash
(pcl) D:\Virtualenv> deactivate
```

### 6.删除虚拟环境

这步是最简单的，一个不当心把虚拟环境玩废了咋办，直接对着虚拟环境文件夹delete即可，然后再重复上面的步骤新建一个就行辣。



到此为止，该说的废话也说的差不多了，该补得知识点也补得差不多，然后就让我们进入重头戏：环境搭建。

# Python-pcl开发环境搭建

强烈建议把以下的流程先看一遍，心里面有个大体的顺序和安装的注意点，然后再返回来一步步安装，这个容错率极低，稍有不慎就是很神秘的bug，哭都没地方哭。

## 准备材料

先让我们看看这个库在windows下有哪些需求，库的官方说法是：

* (Miniconda/Anaconda) - Python 3.5
* pcl 1.8.1(VS2015)
* Cython <= 0.25.2
* Gtk+

之前提交的bug反馈回来了，合作者明确表示
python 3.5 => msvc 2015 of PCL-1.8.1.
python 3.6 => msvc 2017 of PCL-1.8.1 + 升级setuptools到最新版
请安装对应的版本！

由于前面提到的原因，我的电脑已经装上了VS2017，所以VS2015就装不上了，于是本攻略的侧重于VS2017+Python3.6，因此，主要的材料为：

* Windows10 64位操作系统 (强烈要求64位操作系统，32位操作系统最大内存上限4GB，处理点云数据是个很好的冷笑话XD)
* Microsoft Visual C++ Redistributable for Visual Studio 2017 x64版本
    或者省心点，直接下载Build Tools for Visual Studio 2017也行
    ![Visual Studio截图](https://i.loli.net/2020/05/24/R6owdZHGcmW3KlO.png)
    https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017
* Python 3.6.5 Windows x86-64 executable installer，网址是https://www.python.org/downloads/release/python-354/ ，注意选对版本
    ![Python版本](https://i.loli.net/2020/05/24/kEKasjxfh2GVbDi.png)
* numpy‑1.14.3+mkl‑cp36‑cp36m‑win_amd64.whl https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
    下载到PCL_Project文件夹里面，具体的文件名请根据当时的版本号自行改变
* pcl-1.8.1全家桶：PCL-1.8.1-AllInOne-msvc2017-win64.exe https://github.com/PointCloudLibrary/pcl/releases/
* gtk+-bundle_3.10.4-20131202_win64.zip http://win32builder.gnome.org/
    ![GTK截图](https://i.loli.net/2020/05/24/O195KfeTL2YbPCU.png)
    但是有人反应，最近这个网站上不去了，放上我备份的：<a href="https://www.sigmameow.com/blog/files/3/gtk+-bundle_3.10.4-20131202_win64.zip" download="gtk+-bundle_3.10.4-20131202_win64.zip">gtk+-bundle_3.10.4-20131202_win64.zip
</a>
* python-pcl-master 源文件 在这个页面上点击Clone or Download：https://github.com/strawlab/python-pcl
    ![Github截图](https://i.loli.net/2020/05/24/9DOSxT2AyCaXQN5.png)
    把源码解压到PCL_Project文件夹里面，应该获得了python-pcl-master文件夹


有可能随着版本的更新迭代，又不知道从哪里蹦出来神秘的Bug，笔者已经偷偷把目前调试通的所有安装包备份了，如果链接上新了安装失败，可以试试联系我用老版本的看看，800MB全活不打折，放服务器上是不可能放服务器上的，带宽这么低，上传的慢下载的也慢＞︿＜

## 安装

**建议在硬盘的根目录下，专门建立一个文件夹加PCL_Project，所有的东西都往里面安装。**

### 1. Python3.6.5的安装

这个安装主要是为虚拟环境提供对应的版本，为了避免和主Python版本冲突，有一些注意点：

双击运行后出现的界面，Add Python 3.6 to PATH，**一定不要勾选**，当然，如果这是你电脑里面装的第一个Python(小心别被ArcGIS、QGIS、Anaconda等拿了一血)，勾上也行。

![初始选项](https://i.loli.net/2020/05/24/Mc59sxiJgSm7QoY.png)

然后选择自定义安装，不要选Python test Suite

![高级选项](https://i.loli.net/2020/05/24/FKQl1O4skNCELcV.jpg)

下一步，所有的框框都不要勾上，然后自定义路径，避免C:\Program Files\ 等默认的系统路径，不然新建虚拟环境就会提示没有权限执行操作，就算你用管理员模式启动命令提示行，新建的虚拟环境每次也都要用管理员权限启动才行（**血的教训1**）

![自定义选项](https://i.loli.net/2020/05/24/Y8dyQfVwa5ghTk2.png)

然后点安装就可以啦。

### 2. 安装PCL-1.8.1-AllInOne-msvc2017-win64.exe

记得这一步选择选择给所有用户PATH种添加PCL

![PCL第一步Add PCL to the system PATH for all users](https://i.loli.net/2020/05/24/wBaNHQruhV3qzit.png)

然后安装路径一定不要是默认的C:\Program Files，路径越简洁越好，如果路径复杂，他安装到一半跳出来Warning:PATH路径过长，忽略他就好。

![选择安装路径为D:\PCL_Project](https://i.loli.net/2020/05/24/cY6KtHXOiQlJB9I.png)

然后一直下一步，确认两个勾全勾上了，然后点安装

![勾选PCL和3rd Party Library](https://i.loli.net/2020/05/24/EK4LFSOudAMH8tZ.png)

装到一半，不出意外会弹出来这个对话框，让你选择OpenNI2的拓展包，一定不要安装到系统的默认路径C:\Program Files\ 统统装到新建的PCL文件夹里面，如果装到系统路径里了，那么除非你**用管理员权限**启动命令提示行，否则`import pcl`就会报找不到DLL文件的错误（**血的教训2**）

![OpenNI选择根目录D:\PCL_Project](https://i.loli.net/2020/05/24/VoXGJLOjwWIY28x.jpg)

### 3.修改系统环境变量

此电脑>右键>更多>属性

![选择我的电脑属性](https://i.loli.net/2020/05/24/DPGwHNgfeJOErSZ.png)

高级系统设置>高级>环境变量

![设置环境变量](https://i.loli.net/2020/05/24/MNP9cZ73fLEV1y5.png)

新建以下3个环境变量

1. (默认应该就有了) PCL_ROOT：D:\PCL_Project\PCL 1.8.1
2. OPEN_NI2_ROOT： D:\PCL_Project\OpenNI2
3. VTK_ROOT： D:\PCL_Project\PCL 1.8.1\3rdParty\VTK



![输入上面的三个环境变量](https://i.loli.net/2020/05/24/qkAMhnjeTGwNXYD.png)

然后双击Path环境变量，添加4个新字段(注意大小写)
%PCL_ROOT%\bin\
%OPEN_NI2_ROOT%\Tools
%VTK_ROOT%\bin
D:\PCL_Project\OpenNI2\Samples\Bin

![添加4个新字段](https://i.loli.net/2020/05/24/QapYC6jMhOnIl5v.png)

### 4. 创建虚拟环境

用管理员模式启动命令行(Windows Powershell)，依次输入以下代码（理解理解啊，**根据自己的实际情况**和上面的基础知识**适度改编**，注意**>后面**才是要输入的命令，不要复制粘贴这边的代码，要自己敲进去，不然pip install numpy+mkl那一步报错别来找我）

```bash
PS C:\WINDOWS\system32> cd D:\PCL_Project\
PS D:\PCL_Project> Python --version
Python 3.5.4
PS D:\PCL_Project> pip install virtualenv
PS D:\PCL_Project> virtualenv pcl --python=D:\PCL_Project\Python36\python.exe --no-site-packages
Running virtualenv with interpreter D:\Applications\Python36\python.exe
Using base prefix 'D:\\Applications\\Python36'
New python executable in D:\PCL_Project\pcl\Scripts\python.exe
Installing setuptools, pip, wheel…done.
PS D:\PCL_Project> pcl\Scripts\activate
(pcl) PS D:\PCL_Project> pip install cython==0.25.2
Collecting cython==0.25.2
 Downloading
 https://files.pythonhosted.org/packages/74/41/de9dd956efe3eda0759f1ff7854e6322e494c32d3c94a349fc0805873c7a/Cython-0.25.2-cp36-none-win_amd64.whl (2.1MB)
  100% |████████████████████████████████| 2.1MB 1.0MB/s
Installing collected packages: cython
Successfully installed cython-0.25.2
(pcl) PS D:\PCL_Project> pip install numpy-1.14.3+mkl-cp36-cp36m-win_amd64.whl # 注意此处的文件名，不要无脑往里面敲
Processing d:\pcl_project\numpy-1.14.3+mkl-cp36-cp36m-win_amd64.whl
Installing collected packages: numpy
Successfully installed numpy-1.14.3+mkl
```

### 4.5 检查环境变量是否修改成功

```bash
(pcl) PS D:\PCL_Project> python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getenv("PCL_ROOT")
'D:\\PCL_Project\\PCL 1.8.1'   # 成功
>>> os.getenv("PCL_ROOT")
>>> # 啥也没返回，就失败
```

如果啥也没返回，说明环境变量没有被虚拟环境里面的Python读取到，重新检查变量名有没有拼写错误，没有错误的话，关闭命令行，桌面刷新一下，然后上面的步骤，应该就能读出来了

同样的道理，检查`OPEN_NI2_ROOT`、`VTK_ROOT`、`Path`，确认环境变量可以被都出来没错误，再进行下一步

### 5. setup.py的准备工作

打开python-pcl-master文件夹，打开pkg-config文件夹，里面应该有只有3个文件。

![三个文件列表](https://i.loli.net/2020/05/24/cBNuoRXwqZLOJzG.png)

打开gtk+-bundle_3.10.4-20131202_win64.zip，把bin文件夹里面的所有**文件**(86个)，都复制到pkg-config文件夹下面。(注意是复制文件，而不是拷贝文件夹，血的教训3)
复制完成后，pkg-config文件夹应该是乱糟糟的一团（89个文件，而不是pkg-config里面多了个bin文件夹）

到此为止，setup.py的准备工作已经完成了

### 6. 尝试安装python-pcl(从源码编译)

回到刚刚的命令行里面(如果之前环境变量读取失败关掉了的话，记得重新激活虚拟环境)

```bash
(pcl) PS D:\PCL_Project> cd python-pcl-master
(pcl) PS D:\PCL_Project\python-pcl-master> python setup.py build_ext -i
```

然后会出来一大堆疑似乱码的东西，到这里说明离成功很接近了！

耐心等待，如果等待时间很长，电脑还嗡嗡作响留一阵子，结果是这样的话

```bash
pcl_visualization.obj : warning LNK4197: export 'PyInit_pcl_visualization' specified multiple times; using first specification
 Creating library build\temp.win-amd64-3.6\Release\pcl\pcl_visualization.cp36-win_amd64.lib and object build\temp.win-amd64-3.6\Release\pcl\pcl_visualization.cp36-win_amd64.exp
Generating code
Finished generating code
(pcl) PS D:\PCL_Project\python-pcl-master>
```

那就恭喜你了，没有任何问题的编译完成，接下来只要输入以下命令：

```bash
(pcl) PS D:\PCL_Project\python-pcl-master> python setup.py install
……
Using d:\pcl_project\pcl\lib\site-packages
Searching for numpy==1.14.3+mkl
Best match: numpy 1.14.3+mkl
Adding numpy 1.14.3+mkl to easy-install.pth file

Using d:\pcl_project\pcl\lib\site-packages
Finished processing dependencies for python-pcl==0.3
(pcl) PS D:\PCL_Project\python-pcl-master>
```

出来上面的提示，就大功告成了！

但是出来这个报错的话：

```bash
LINK : fatal error LNK1104: cannot open file 'libboost_date_time-vc140-mt-1_64.lib'
error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\link.exe' failed with exit status 1104
(pcl) PS D:\PCL_Project\python-pcl-master>
```

那还要恭喜你，因为这个问题我已经解决了
学会看一下报错，报错讲了啥？说的是打不开那个文件，那我们看看那个文件到底有啥猫腻

这里采用了everything文件搜索工具，文件秒搜你值得拥有（看看就行了，不是重点）

![everything搜索结果](https://i.loli.net/2020/05/24/s5VgPSl8dAaKTOb.png)

很明显，是vc140和vc141的文件名出错，然后我们打开那个文件路径
D:\PCL_Project\PCL 1.8.1\3rdParty\Boost\lib
就会发现：

![文件夹界面](https://i.loli.net/2020/05/24/AfnipU1sEoWaY8j.png)

他喵的好像文件名全都不对啊，然后你就把原来的lib文件夹复制一份，改名位lib.old文件夹，然后用鼠标+键盘，把所有的vc141都改成vc140即可

不出意外应该就打包完成啦。

### 7. 功能测试

激活虚拟环境

```bash
(pcl) PS D:\PCL_Project> python
>>> import pcl
>>>
```

说明安装成功！继续进行功能测试看看

```python
>>> import pcl
>>> import numpy as np
>>> p = pcl.PointCloud(np.array([[1, 2, 3], [3, 4, 5]], dtype=np.float32))
>>> seg = p.make_segmenter()
>>> seg.set_model_type(pcl.SACMODEL_PLANE)
>>> seg.set_method_type(pcl.SAC_RANSAC)
>>> indices, model = seg.segment()
[pcl::SampleConsensusModel::getSamples] Can not select 0 unique points out of 2!
[pcl::RandomSampleConsensus::computeModel] No samples could be selected!
[pcl::SACSegmentation::segment] Error segmenting the model! No solution found.
>>>
```

当然在普通命令行里面（非管理员模式）还有几率遇到这个报错

```python
>>> import pcl
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "D:\Virtualenv\pcl\lib\site-packages\python_pcl-0.3-py3.5-win-amd64.egg\pcl\__init__.py", line 2, in <module>
  from ._pcl import *
ImportError: DLL load failed: 找不到指定的模块。
```

有大佬 https://github.com/strawlab/python-pcl/issues/155 用工具定位了一下，发现是OpenNI2.dll没找到，于是把C:\Program Files\OpenNI2\Samples\Bin，这个里面含有OpenNI2.dll, 添加到Path环境变量就行了（这一点已经在上面环境变量那一步修改完成了），至于为什么不建议安装到默认的C:\Program Files里面呢，因为这么操作完，只有在管理员模式下import pcl才不会报错，到普通的IDE里面就同样的报错，因为不开管理员，就没有权限使用系统文件夹里面的文件，盲生你终于发现了华点。

如果修改了环境变量依然不能解决的话，找到D:\PCL_Project\PCL 1.8.1\3edParty\OpenNI2\OpenNI-Windows-x64-2.2.msi，双击运行，选择Repair后重启即可。

开源带来了商业软件所不具有的免费优势，但是带来的就是复杂的调试过程和看作者心情的说明文档，开源带来的最明显变化，即从商业公司里程序员头发逐渐消失，变为所有用户头发一起逐渐消失

如有任何问题，欢迎联系笔者[whz@sigmameow.com](mailto:whz@sigmameow.com)或者在评论区留言，携手共同解决问题！

如果这篇文章成功的帮你解决了一个难题，请不要吝啬一瓶防脱护发素的钱哦(￣▽￣)"

| 支付宝二维码 | 微信二维码 |
| :------: | :------: |
| <img width="256" class="mb-4 rounded" alt="" src="https://i.loli.net/2020/04/01/dCpK8TgnL4xurk6.jpg"> | <img width="256" class="mb-4 rounded" alt="" src="https://i.loli.net/2020/04/01/ZagHx9wRiYQ1Cq2.png"> |