from traits.api import HasTraits, Button, Int
from traitsui.api import View, Item

class ButtonEditor(HasTraits):
    my_button = Button(u'+1s')
    counter = Int(365*80*12*3600)

    # 创建视图
    traits_view = View(
        Item('my_button', label=u'膜一下'),
        Item('counter', label=u'天命'),
        title=u'蛤', buttons = ['OK'], resizable=True)

    # 当按钮点击后，处理触发的事件
    def _my_button_fired(self):
        self.counter += 1

button = ButtonEditor()
button.configure_traits()
