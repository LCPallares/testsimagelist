import json
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kivymd.uix.imagelist import SmartTileWithLabel

Builder.load_string("""
<MiPantalla@BoxLayout>
    orientation: 'vertical'
    MDToolbar:
        id: toolbar
        #title: app.title
        left_action_items: [['menu', lambda x: None]]
        elevation: 10
        md_bg_color: app.theme_cls.primary_color

    ScrollView:

        Contenedor:
            id: mdlt
            cols: 3
            row_default_height:
                (self.width - self.cols*self.spacing[0])/self.cols
            row_force_default: True
            size_hint_y: None
            height: self.minimum_height
            padding: dp(4), dp(4)
            spacing: dp(4)

""")

with open('wlop.json', 'r') as openfile:
    datos = json.load(openfile)


class Contenedor(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for dato in datos:
            teja = SmartTileWithLabel(
                source=dato['miniaturas'],
                mipmap=True,
                font_style='Subtitle1',
                text=dato['titulo'])
            teja.bind(on_press=self.callback)
            self.add_widget(teja)

    def callback(self, instance):
        print(f'{instance.text} es el texto')


class Test(MDApp):
    def __init__(self, **kwargs):
        self.title = "tejas"
        super().__init__(**kwargs)

    def build(self):
        root = Factory.MiPantalla()
        return root


if __name__ == '__main__':
    Window.size = (361, 641)
    Test().run()
