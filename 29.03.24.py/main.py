from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.utils import platform
from random import randint
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.properties import NumericProperty


class MenuScreen (Screen) :
    def __init__(self, **kwargs):
        super().__init__(** kwargs)

class GameScreen (Screen) :
    points = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(** kwargs)
        
    def on_enter(self, *args):
        self.ids.planet.new_planet()
        return super().on_enter(*args)

class Planet(Image):
    is_anim = False
    hp = None
    planet = None
    planet_index = 0
      
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.points += 1
            self.hp -= 1
            if self.hp <=0:
                self.new_planet()
                
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y=y-5, duration=0.05) + \
            Animation(x=x, y=y, duration=0.05)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self,'is_anim', False)
        return super().on_touch_down(touch)

    def new_planet(self):
        self.planet = app.LEVELS[randint(0, len(app.LEVELS)) -1]
        self.source = app.PLANETS[self.planet]['source']
        self.hp = app.PLANETS[self.planet]['hp']
    
class MainApp(App):
    LEVELS = ['Mercury', 'Venus', 'Earth', 'Mars',
              'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    PLANETS = {
        'Mercury': {"source": 'assets/Image/1.png', 'hp': 10},
        'Venus': {"source": 'assets/Image/2.png', 'hp': 20},
        'Earth': {"source": 'assets/Image/3.png', 'hp': 30},
        'Mars': {"source": 'assets/Image/4.png', 'hp': 40},
        'Jupiter': {"source": 'assets/Image/5.jpg', 'hp': 50},
        'Saturn': {"source": 'assets/Image/6.png', 'hp': 60},
        'Uranus': {"source": 'assets/Image/7.png', 'hp': 80},
        'Neptune': {"source": 'assets/Image/3.png', 'hp': 100},
    }
    def build(self):
        sm= ScreenManager()
        sm.add_widget(MenuScreen(name ='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm
    
    if platform != 'android':
        Window.size = (400,600)
        Window.left = 500
        Window.top = 100      
    
app = MainApp()
app.run()