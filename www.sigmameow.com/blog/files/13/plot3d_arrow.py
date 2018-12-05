# -*- coding:utf-8 -*-
from tvtk.api import tvtk
from tvtkfunc import ivtk_scene, event_loop

# 读取Plot3D数据
plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",   # 网格文件
        q_file_name="combq.bin",   # 空气动力学结果文件
        scalar_function_number=100,  # 设置标量数据数量
        vector_function_number=200)  # 设置矢量数据数量
plot3d.update()   # 让Plot3D计算其输出数据
grid = plot3d.output.get_block(0)   # 获取读入的数据集对象

# 数据随机选取
## 对数据集中的数据进行随机选取，每50个点选择一个点
mask = tvtk.MaskPoints(random_mode=True, on_ratio=50)
mask.set_input_data(grid)
## 创建表示箭头的PolyData数据集
glyph_source = tvtk.ArrowSource()

# 绘制箭头
## 在Mask采样后的PolyData数据集每个点上放置一个箭头
## 箭头的方向、长度和颜色由与点对应的矢量和标量数据决定
glyph = tvtk.Glyph3D(input_connection=mask.output_port, scale_factor=4)
glyph.set_source_connection(glyph_source.output_port)
## 绘制数据
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range, input_connection=glyph.output_port)
a = tvtk.Actor(mapper=m)

# 窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()