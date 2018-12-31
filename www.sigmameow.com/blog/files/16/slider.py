from traits.api import HasTraits, Int, Range, Property, property_depends_on
from traitsui.api import View, Item, RangeEditor

class RangeDemo(HasTraits):
    a = Range(1, 10)
    b = Range(1, 10)
    c = Property(Int)
    view = View(
        Item('a'),
        Item('b'),
        '_',  # 添加分割线
        Item('c'),
        Item('c', editor=RangeEditor(low=1, high=20, mode='slider'),),
        title="滑动计算器",width=0.3
    )
    
    @property_depends_on('a,b', settable=True)
    def _get_c(self):
        print('计算中...')
        return (self.a + self.b)
    
range_domo = RangeDemo()
range_domo.configure_traits()