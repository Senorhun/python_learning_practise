# pip install kivy

from kivy.app import App
from kivy.uix.label import Label

class HellóApp(App):
    def build(self):
        return Label(text='Helló, Kivy világ!')

HellóApp().run()
