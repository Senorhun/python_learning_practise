from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ElrendezésApp(App):
    def build(self):
        fő_elrendezés = BoxLayout(orientation='vertical')

        első_sor = BoxLayout(orientation='horizontal')
        első_sor.add_widget(Label(text='1/1'))
        első_sor.add_widget(Label(text='1/2'))
        fő_elrendezés.add_widget(első_sor)

        második_sor = BoxLayout(orientation='horizontal')
        második_sor.add_widget(Label(text='2/1'))
        második_sor.add_widget(Label(text='2/2'))
        fő_elrendezés.add_widget(második_sor)

        return fő_elrendezés

ElrendezésApp().run()
