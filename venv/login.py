from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Window.size = 320,568

def kivy_color(rgb_color):
    return rgb_color/255

class User:
    def __init__(self,type='Guest'):
        self.type = type
        self.user_photo = 'circle_goat.png'
        self.username = ''
        self.password = ''
        self.nickname = 'goat'

class MainWindow(Screen):
    login_database = {'Andrewis2431': 'andrej', 'CHAD': 'actuallychad'}
    #Touch(reset)

    def press_log_in(self):
        if self.login.text in self.login_database and \
            self.login_database[self.login.text] == self.password.text:
                self.app.user.username = self.login.text
                self.app.user.nickname = self.login.text
                self.app.user.password = self.password.text
                self.manager.next_screen.nickname_label.text = self.login.text
                self.next_screen()
        else:
            for text in (self.login,self.password):
                self.clear_text(text)
            self.warning = Label(text = "Wrong login/password!",size_hint=(.7, .2),pos_hint={'x': .15, 'top': .75},color=(0.8, 0, 0, 0.8),font_size='15sp')
            self.float_layout.add_widget(self.warning)
            Clock.schedule_once(self.delete_warning, 3)

            markup: True
            text: "[b][i]To Gather"

    def delete_warning(self,*args):
        self.float_layout.remove_widget(self.warning)
    def clear_text(self,text):
        text.text = ''

    def next_screen(self):
        print('here')
        self.manager.current = "next_screen"

    def nickname_screen(self):
        self.manager.current = "nickname_screen"




class NicknameWindow(Screen):

    def press_continue(self):
        if self.nickname.text != '':
            self.app.user.nickname = self.nickname.text
            self.manager.next_screen.nickname_label.text = self.nickname.text
            self.manager.current = "next_screen"

    def return_to_homescreen(self):
        self.manager.current = 'login_screen'




class SecondWindow(Screen):
    def return_to_homescreen(self):
        self.manager.current = 'login_screen'



class MyManager(ScreenManager):
    def __init__(self,**kwargs):
        super(MyManager,self).__init__(**kwargs)

class Image_Button(ButtonBehavior,Image):
    def __init__(self,**kwargs):
        super(Image_Button, self).__init__(**kwargs)
        self.source = 'circle_goat.png'

    def on_press(self):
        print('opening profile')


kv = Builder.load_file("login.kv")
class GooutApp(App):
    def __init__(self,**kwargs):
        super(GooutApp, self).__init__(**kwargs)
        print(7)
        self.user = User()
    def build(self):

        m = MyManager()
        return m

if __name__ == "__main__":
     GooutApp().run()