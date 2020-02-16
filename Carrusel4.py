# http://danlec.com/st4k#questions/47188642
import json
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage


with open('wlop.json', 'r') as openfile:
    datos = json.load(openfile)

# print(datos['miniaturas'])


class CarouselApp(App):

    def build(self):
        carousel = Carousel(direction='bottom')

        for dato in datos:
            # print(dato['miniaturas'])
            image = AsyncImage(source=dato['miniaturas'], allow_stretch=True)
            carousel.add_widget(image)

        return carousel


CarouselApp().run()
