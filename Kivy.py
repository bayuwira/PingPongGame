import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class myGrid(GridLayout):
    #buat design tabel secara keras/langsung dari file python, langsung di coding
    def __init__(self, **kwargs):
        super(myGrid, self).__init__(**kwargs)
        self.cols = 1

        self.secondGrid = GridLayout()
        self.secondGrid.cols = 2

        self.secondGrid.add_widget(Label(text = "Nama : "))
        self.name = TextInput(multiline=False)
        self.secondGrid.add_widget(self.name)

        self.secondGrid.add_widget(Label(text="Email : "))
        self.email = TextInput(multiline=False)
        self.secondGrid.add_widget(self.email)

        self.secondGrid.add_widget(Label(text="Program Studi : "))
        self.programStudi = TextInput(multiline=False)
        self.secondGrid.add_widget(self.programStudi)

        self.add_widget(self.secondGrid)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        email = self.email.text
        programStudi = self.programStudi.text

        print("Name : {}\nemail : {}\nprogram studi : {}".format(name, email, programStudi))
        self.name.text = ""
        self.email.text = ""
        self.programStudi.text = ""

class myGrid2(Widget):
    #mygrid 2 memiliki class design sendiri seperti .css yaitu .kv dengan penamaan yg sama seperti nama file atau nama main class
    name1 = ObjectProperty(None) #penaamaan di file .kv samain sama objeknya
    emailvar = ObjectProperty(None)
    coursex = ObjectProperty(None)

    def button(self):
        print("Name: {}\nEmail: {}\nCourse: {}".format(self.name1.text, self.emailvar.text, self.coursex.text))
        self.name1.text = ""
        self.emailvar.text = ""
        self.coursex.text = ""

class Latihan1App(App):
    def build(self):
        return myGrid2()


if __name__ == "__main__":
    Latihan1App().run()