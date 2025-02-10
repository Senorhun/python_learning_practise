from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class KöszönApp(App):
    def build(self):
        fő_elrendezés = BoxLayout(orientation='vertical')

        név_elrendezés = BoxLayout(orientation='horizontal')
        név_felirat = Label(text='Név:')
        név_elrendezés.add_widget(név_felirat)
        self.név_bevitel = TextInput(text='Csaba', multiline=False)
        név_elrendezés.add_widget(self.név_bevitel)
        fő_elrendezés.add_widget(név_elrendezés)

        nyomógomb = Button(text='Kattints')
        nyomógomb.bind(on_press=self.nyomógomb_lenyomva)
        fő_elrendezés.add_widget(nyomógomb)

        self.köszöntés_felirat = Label(text='Szia!')
        fő_elrendezés.add_widget(self.köszöntés_felirat)

        return fő_elrendezés
    
    def nyomógomb_lenyomva(self, példány):
        self.köszöntés_felirat.text = f'Szia, {self.név_bevitel.text}!'

KöszönApp().run()
