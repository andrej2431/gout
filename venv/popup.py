from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass
kv = Builder.load_file("popup.kv")

class MyApp(App):
    def build(self):
        return kv

def show_popup():
    show = P()
    popupWindow = Popup(title="FREE MONEY!!!", content=show,size_hint=(None,None),size=(400,400))
    popupWindow.open()


if __name__ == "__main__":
     MyApp().run()