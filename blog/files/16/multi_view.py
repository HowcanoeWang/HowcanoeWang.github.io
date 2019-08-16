from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group

class ModelManager(HasTraits):
    model_name = Str
    category = Str
    model_file = Str
    model_number = Int
    vertices = Int

    view_cn = View(
        Group(
            Item('model_name', label=u"模型名称"),
            Item('model_file', label=u"文件名", tooltip=u"路径及文件名"),
            Item('category', label=u"模型类型"),
            label=u"模型信息", show_border=True),
        Group(
            Item('model_number', label=u"模型数量"),
            Item('vertices', label=u"顶点数量"),
            label=u"统计数据", show_border=True),
        title=u"模型资料", width=200, resizable=True
    )

    view_en = View(
        Group(
            Item('model_name', label=u"Model Name"),
            Item('model_file', label=u"File Name", tooltip=u"Path and File Name"),
            Item('category', label=u"Model Type"),
            label=u"Model Info", show_border=True),
        Group(
            Item('model_number', label=u"Model Number"),
            Item('vertices', label=u"Vertices Number"),
            label=u"Statistics", show_border=True),
        title=u"Model Data", width=200, resizable=True
    )

view_jp = View(
    Group(
        Item('model_name', label=u"モデル名"),
        Item('model_file', label=u"ファイル名", tooltip=u"パスとファイル名"),
        Item('category', label=u"モデルの種類"),
        label=u"モデル情報", show_border=True),
    Group(
        Item('model_number', label=u"モデル数"),
        Item('vertices', label=u"頂点数"),
        label=u"統計データ", show_border=True),
    title=u"モデルデータ", width=200, resizable=True
)

model = ModelManager()
model.configure_traits(view=view_jp)