from kivy.app import App
from kivy.uix.button import Button

class EseményApp(App):
    def build(self):
        nyomógomb = Button(text='Kattints!')
        nyomógomb.bind(on_press=self.kattintás)
        return nyomógomb

    def kattintás(self, példány):
        print('Kattintás')

EseményApp().run()
