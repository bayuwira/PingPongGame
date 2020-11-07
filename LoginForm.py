from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("loginform.kv")

class LoginFormApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    LoginFormApp().run()