from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable',(0))
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import random
from kivy.uix.button import Button
phoneRes= (400, 400)
Window.size = (400, 480)
import winsound
import threading
frequency = 500
duration = 100
tiles = globals()

def shittymusic():
    qr = random.randint(500,550)
    wr = random.randint(800,1000)
    winsound.Beep(qr,wr)

def playshittymusic():
    x = 5
    while x > 0 :
        threading.Thread(target= shittymusic).start()
        x = x-1

threading.Thread(target=playshittymusic).start()

gameInterface = BoxLayout()

class main_layout(FloatLayout):
    def __init__(self,**kwargs):
        super(main_layout, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)

class character(Button):

    def __init__(self,stats,**kwargs):
        super(character, self).__init__(**kwargs)
        self.stats = stats
        self.position = (((self.pos[1]) - 2) / 40) - 1, self.pos[0] / 40

    def update_pos(self):
        self.position = (((self.pos[1]) - 2) / 40) - 1, self.pos[0] / 40
        self.stats=tiles["tile"+str((((self.pos[1]) - 2) / 40) - 1)+"_"+str(self.pos[0] / 40)].text
        print self.stats
        if self.stats == "apple":
            self.text = ":)"
            winsound.Beep(1000, 100)
            winsound.Beep(1700, 100)
            tiles["tile"+str(self.position[0])+"_"+str(self.position[1])].color = (0,0,0,0)
            tiles["tile" + str(self.position[0]) + "_" + str(self.position[1])].text = "_"

    def move_up (self,*args):
        if self.position[0] >= 9:
            return
        self.pos = (self.pos[0],self.pos[1]+40)
        winsound.Beep(frequency, duration)
        winsound.Beep(700, 67)
        self.update_pos()

    def move_left (self,*args):
        if self.position[1] <= 0 :
            return
        self.pos = (self.pos[0]-40,self.pos[1])
        winsound.Beep(frequency, duration)
        winsound.Beep(700, 67)
        self.update_pos()

    def move_right (self,*args):
        if self.position[1] >= 9:
            return
        self.pos = (self.pos[0]+40,self.pos[1])
        winsound.Beep(frequency, duration)
        winsound.Beep(700, 67)
        self.update_pos()
    def move_down (self,*args):
        if self.position[0] <= 0:
            return
        self.pos = (self.pos[0],self.pos[1]-40)
        winsound.Beep(frequency, duration)
        winsound.Beep(700, 67)
        self.update_pos()

map = main_layout()

for x in range(2,12):
    for i in range(0,10):

        tiles["tile"+str(str(x-2)+"_"+str(i))] = Button(color=(0, 0, 0, 0),pos=(i*40, x*40),size_hint=(None, None), size=(40, 40),text=str(str(x-2)+"-"+str(i)),font_size=10, id=str(str(x)+"-"+str(i)))
        map.add_widget(tiles["tile"+str(str(x-2)+"_"+str(i))])

applex = random.randint(0,9)
appley = random.randint(0,9)

tiles["tile"+str(applex)+"_"+str(appley)].text="apple"
tiles["tile"+str(applex)+"_"+str(appley)].color=(100, 0, 0, 10)

player_x = random.randint(0, 9)
player_y = random.randint(0, 9)
player = character("0",pos=(player_x*40,player_y*40),size_hint=(None, None), size=(40, 40),text="@",color=(200, 100, 200, 10),background_normal="")

map.add_widget(player)

buttonbox = BoxLayout(orientation="horizontal",pos_hint={'center_y':0.085, 'center_x': 0.5},size_hint=(1,0.165))

up = Button(text="up")
down = Button(text="down")
right = Button(text="right")
left = Button(text="left")

buttonbox.add_widget(up)
buttonbox.add_widget(down)
buttonbox.add_widget(left)
buttonbox.add_widget(right)
map.add_widget(buttonbox)

up.bind(on_press=player.move_up)
down.bind(on_press=player.move_down)
left.bind(on_press=player.move_left)
right.bind(on_press=player.move_right)

class MainApp(App):
    def build(self):

        return map

MainApp().run()

