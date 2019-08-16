# -*- coding:utf-8 -*-
import numpy as np
from mayavi import mlab

# 建立数据
x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)
# 数据可视化
mlab.figure(bgcolor=(1,1,1))   # 设置背景色
surf = mlab.surf(z, colormap='cool')

# 访问surf对象的LUT
lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()
# lut是一个255*4的数组，每一列表示RGBA(红、绿、蓝、透明图层)，范围0-255
lut[:, -1] = np.linspace(0, 255, 256)   # 修改alpha通道增加透明度
# 将修改好的LUT保存到surf对象中
surf.module_manager.scalar_lut_manager.lut.table = lut

# 更新视图并显示出来
mlab.show()