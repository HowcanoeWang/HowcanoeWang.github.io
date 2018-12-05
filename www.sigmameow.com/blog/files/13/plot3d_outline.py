# -*- coding:utf-8 -*-
from tvtk.api import tvtk
from tvtk.common import configure_input
from tvtkfunc import ivtk_scene, event_loop

# 读取Plot3D数据
plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",   # 网格文件
        q_file_name="combq.bin",   # 空气动力学结果文件
        scalar_function_number=100,  # 设置标量数据数量
        vector_function_number=200)  # 设置矢量数据数量
plot3d.update()   # 让Plot3D计算其输出数据
grid = plot3d.output.get_block(0)   # 获取读入的数据集对象

# 创建等值面
con = tvtk.ContourFilter()   # 创建等值面对象
con.set_input_data(grid)
con.generate_values(10, grid.point_data.scalars.range)   # 指定轮廓数和数据范围

# 计算轮廓线
outline = tvtk.StructuredGridOutlineFilter()   # 计算表示外边框的PolyData对象
configure_input(outline, grid)   # 调用tvtk.common.configure_input()
# 绘制
m = tvtk.PolyDataMapper(input_connection=outline.output_port)
a = tvtk.Actor(mapper=m)
a.property.color = 0.3, 0.5, 0.3

# 窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()