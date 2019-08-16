# -*- coding:utf-8 -*-
import numpy as np
from mayavi import mlab

# 数据准备
city = ['BeiJing','HongKong','Sao Paulo','Toronto','San Francisco','Sydney']
long = np.array([116.23, 114.19, -46.63, -79.38, -122.45, 151.21])
lat  = np.array([39.54, 22.38, -23.53, 43.65, 37.77, -33.87])

# 将经纬度转换为三维坐标
x = np.cos(np.deg2rad(lat)) * np.cos(np.deg2rad(long))
y = np.cos(np.deg2rad(lat)) * np.sin(np.deg2rad(long))
z = np.sin(np.deg2rad(lat))

# 建立窗口
mlab.figure(bgcolor=(0.48, 0.48, 0.48), size=(400, 400))

# 绘制半透明体地球
sphere = mlab.points3d(0, 0, 0,   # 地球中心点为原点
                       scale_factor=2,   #  符号放缩的比例
                       color=(0.67, 0.77, 0.93),   # 地球颜色
                       resolution=50,   # 球体(正多面体)的面数
                       opacity=0.7,   # 透明度70%
                       name='Earth')
sphere.actor.property.specular = 0.45   # 设置镜面反射参数（打高光）
sphere.actor.property.specular_power = 5   # 设置高光柔和度
sphere.actor.property.backface_culling = True   # 提出背面，达到更好的透明效果

# 绘制城市
points = mlab.points3d(x, y, z, scale_factor=0.03, color=(0, 0, 1))   # 城市位置用点表示
for i, city_name in enumerate(city):   # 对每一个城市名
    label = mlab.text(x[i], y[i], city_name, z=z[i],
                      color=(0, 0, 0),  # 城市名字体颜色
                      width=0.016*len(city_name),   # 标签宽度
                      name=city_name)

# 绘制大洲边界
from mayavi.sources.builtin_surface import BuiltinSurface
continents_src = BuiltinSurface(source='earth', name='Continents')   # 导入自带的大洲边界
continents_src.data_source.on_ratio = 2   # 设置LOD为2
continents = mlab.pipeline.surface(continents_src, color=(0,0,0))  # 在球表面上绘制边界

# 绘制赤道
theta = np.linspace(0, 2 * np.pi, 100)   # 平分360度为100份
x = np.cos(theta)
y = np.sin(theta)
z = np.zeros_like(theta)
mlab.plot3d(x, y, z, color=(0.5, 0.1, 0.1), opacity=0.2, tube_radius=None)

#  显示可交互窗口
mlab.view(100, 60, 40, [-0.05, 0, 0])
mlab.show()