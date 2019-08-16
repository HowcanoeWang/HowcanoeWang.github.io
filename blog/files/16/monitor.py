# -*- coding:utf-8 -*-
from traits.api import HasTraits, Str, Int, Event, on_trait_change

class Child(HasTraits):
    name = Str
    position = Int(0)  # 默认0是刚进门的第一块地砖
    doing = Str('发呆')
    call = Event

    def __str__(self):
        return f'{self.name}(编号{id(self)})'

    # 静态监听position属性的变化
    def _position_changed(self, old, new):
        print(f'[静态命名]:<位置监听>{self}[位置]从{old}变成了{new}')

    # 静态监听任何属性的变化
    def _anytrait_changed(self, name, old, new):
        print(f'[静态命名]:<全面监听>{self}的[{name}]值从{old}变成了{new}')

    # 静态@修饰，只要doing发生了改变，就调用lalala函数，这边的函数命名就不用遵循监听函数命名规则了
    @on_trait_change("doing")  # 想监听多个属性，把“doing”改成“name, doing”即可
    def lalala(self):
        print(f'[静态修饰]:<行为监听>检测到{self}的doing值改变了')

    # event监听，只要对call进行赋值，就会调用这个函数，并更改行为
    def _call_fired(self):
        print(f'<事件监听>{self}意识到你在叫TA')
        self.doing = '转头看你'


# 重点关注对象，这里采用动态监听
def important(obj, name, old, new):
    print(f'[动态监听]:<重点关注>的{obj}的{name}属性，从{old}变成了{new}')