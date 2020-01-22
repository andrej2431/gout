import kivy
from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color,Line


#class MyGrid(Widget):
    #name = ObjectProperty(None)
    #email = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(MyGrid,self).__init__(**kwargs)
    #     self.cols = 1
    #
    #     #
    #     self.inside = GridLayout()
    #     self.inside.cols = 2
    #
    #     self.inside.add_widget(Label(text = "First Name: "))
    #     self.first_name = TextInput(multiline=False)
    #     self.inside.add_widget(self.first_name)
    #
    #     self.inside.add_widget(Label(text="Last Name: "))
    #     self.last_name = TextInput(multiline=False)
    #     self.inside.add_widget(self.last_name)
    #
    #     self.inside.add_widget(Label(text="Email: "))
    #     self.email = TextInput(multiline=False)
    #     self.inside.add_widget(self.email)
    #
    #     self.add_widget(self.inside)
    #     #
    #     self.submit = Button(text = 'Submit', font_size=30)
    #     self.submit.bind(on_press=self.pressed)
    #     self.add_widget(self.submit)
    #
    #def btn(self):
        #print("Name:",self.name.text, "Email: ",self.email.text)
        #self.name.text = ''
        #self.email.text = ''


class Touch(Widget):
    btn = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Touch,self).__init__(**kwargs)
        with self.canvas:
            Line(points=(30,30,50,50,70,30))
            Color(1,0,0,.5,mode='rgba')
            self.rect = Rectangle(pos=(0,0),size=(50,50))
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        print('Mouse Down',touch)
        self.rect.pos = touch.pos
    def on_touch_move(self, touch):
        print('Mouse move',touch)
        self.rect.pos = touch.pos
    def on_touch_up(self, touch):
        print('Mouse up',touch)
        self.opacity = 1

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()
