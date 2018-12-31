from traits.api import HasTraits, Instance, Range, on_trait_change
from traitsui.api import View, Item, Group
from mayavi.core.api import PipelineBase
from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor    # 上一个例子的那些导入，其实都在API里面
from numpy import arange, pi, cos, sin


dphi = pi/300.
phi = arange(0.0, 2*pi + 0.5*dphi, dphi, 'd')
def curve(n_mer, n_long):
    mu = phi*n_mer
    x = cos(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    y = sin(mu) * (1 + cos(n_long * mu/n_mer)*0.5)
    z = 0.5 * sin(n_long*mu/n_mer)
    t = sin(mu)
    return x, y, z, t


# 1. 建立从HasTraits继承的类
class MyModel(HasTraits):
    n_meridional = Range(0, 30, 6)
    n_longitudinal = Range(0, 30, 11)
    # 场景模型
    scene = Instance(MlabSceneModel, ())  # 返回一个MlabSceneModel的实例
    # 管线实例
    plot = Instance(PipelineBase)

    #当场景被激活，或者参数发生改变，更新图形
    @on_trait_change('n_meridional,n_longitudinal,scene.activated')
    def update_plot(self):
        x, y, z, t = curve(self.n_meridional, self.n_longitudinal)
        if self.plot is None:#如果plot未绘制则生成plot3d
            self.plot = self.scene.mlab.plot3d(x, y, z, t,
                        tube_radius=0.025, colormap='Spectral')
        else:#如果数据有变化，将数据更新即重新赋值
            self.plot.mlab_source.set(x=x, y=y, z=z, scalars=t)

    # 建立View视图
    view = View(Item(name='scene',
                     editor=SceneEditor(scene_class=MayaviScene),
                     show_label=False,
                     resizable=True,
                     height=500,
                     width=500
                     ),
                Group(Item('n_meridional', label='经度方向'),
                      Item('n_longitudinal', label='纬度方向')),
                title='场景查看器',
                resizable=True
                )

a = MyModel()
a.configure_traits()