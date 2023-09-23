from kivy.app import App
# from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from python import backend
# Config.set("graphics", "resizable", 0)
# Config.set("graphics", "width", 400)
# Config.set("graphics", "height", 500)

class MainApp(App, backend):
    def update_label(self):
        self.lbl.text = self.formula

    def add_numbers(self, instance):
        if (str(instance.text) == "√"):
            self.formula += "#"
        else:
            self.formula += str(instance.text)
        print(str(instance.text))
        self.update_label()

    def add_result(self, instance):
        self.lbl.text = self.osnova()
        self.formula = ""

    def add_del(self, instance):
        a = len(self.lbl.text)
        self.lbl.text = self.lbl.text[:a-1]
        self.formula = self.lbl.text

    def add_ac(self, instance):
        self.formula = ""
        self.lbl.text = self.formula

    def build(self):
        self.formula = ""
        bl = BoxLayout(orientation = "vertical", padding = 25)
        gl = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = Label(text="0", font_size = 40, size_hint = (1, .4))

        bl.add_widget( self.lbl )

        gl.add_widget(Button(text="Ac", on_press = self.add_ac))
        gl.add_widget(Button(text="DEL", on_press = self.add_del))
        gl.add_widget(Button(text="#", on_press = self.add_numbers))
        gl.add_widget(Button(text="/", on_press = self.add_numbers))

        gl.add_widget(Button(text="7", on_press = self.add_numbers))
        gl.add_widget(Button(text="8", on_press = self.add_numbers))
        gl.add_widget(Button(text="9", on_press = self.add_numbers))
        gl.add_widget(Button(text="*", on_press = self.add_numbers))

        gl.add_widget(Button(text="4", on_press = self.add_numbers))
        gl.add_widget(Button(text="5", on_press = self.add_numbers))
        gl.add_widget(Button(text="6", on_press = self.add_numbers))
        gl.add_widget(Button(text="-", on_press = self.add_numbers))

        gl.add_widget(Button(text="1", on_press = self.add_numbers))
        gl.add_widget(Button(text="2", on_press = self.add_numbers))
        gl.add_widget(Button(text="3", on_press = self.add_numbers))
        gl.add_widget(Button(text="+", on_press = self.add_numbers))

        gl.add_widget(Widget())
        gl.add_widget(Button(text = "0", on_press = self.add_numbers))
        gl.add_widget(Button(text = ".", on_press = self.add_numbers))
        gl.add_widget(Button(text = "=", on_press = self.add_result))

        bl.add_widget(gl)

        return bl

if __name__ == "__main__":
    MainApp().run()
