from numpy import sqrt, sin, mgrid
from traits.api import HasTraits, Instance
from traitsui.api import View, Item
from mayavi.tools.mlab_scene_model import MlabSceneModel  # Mlab的容器，可以让我们在TraitsUI的视图中使用Mayavi的Scene
from mayavi.core.ui.mayavi_scene import MayaviScene   # 提供了Mayavi视图的工具栏、相机视角交互、坐标轴等等
from tvtk.pyface.scene_editor import SceneEditor  # 基于SceneModel实例的TraitsUI编辑器

# 1. 建立从HasTraits继承的类
class ActorViewer(HasTraits):
    # 场景模型
    scene = Instance(MlabSceneModel, ())  # 返回一个MlabSceneModel的实例
    # 建立View视图
    view = View(Item(name='scene',
                     editor=SceneEditor(scene_class=MayaviScene),
                     show_label=False,
                     resizable=True,
                     height=500,
                     width=500
                     ),
                title='场景查看器',
                resizable=True
                )

    # 定义初始化方法__init__，生成数据
    def __init__(self, **traits):
        HasTraits.__init__(self, **traits)
        self.generate_data()  # 生成数据并绘制

    def generate_data(self):
        # 准备数据
        X, Y = mgrid[-2:2:100j, -2:2:100j]
        R = 10 * sqrt(X ** 2 + Y ** 2)
        Z = sin(R) / R
        # 显示数据
        self.scene.mlab.surf(X, Y, Z, colormap='cool')

a = ActorViewer()
a.configure_traits()