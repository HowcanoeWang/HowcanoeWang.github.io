# -*- coding:utf-8 -*-
import numpy as np
from mayavi import mlab

# 建立数据
x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)
# 数据可视化
mlab.figure(bgcolor=(1,1,1))   # 设置背景色
surf = mlab.surf(z, colormap='cool')
# 更新视图并显示出来
mlab.show()