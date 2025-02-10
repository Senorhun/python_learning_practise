from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SzámológépApp(App):
    def build(self):
        self.műveletek = ['/', '*', '+', '-']
        fő_elrendezés = BoxLayout(orientation='vertical')
        self.megoldás = TextInput(multiline=False, readonly=True, halign='right', font_size=50)
        fő_elrendezés.add_widget(self.megoldás)
        for sor in [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+'],
        ]:
            vízszintes_elrendezés = BoxLayout()
            for felirat in sor:
                aktuális_nyomógomb = Button(text=felirat)
                aktuális_nyomógomb.bind(on_press=self.nyomógomb_lenyomva)
                vízszintes_elrendezés.add_widget(aktuális_nyomógomb)
            fő_elrendezés.add_widget(vízszintes_elrendezés)
        return fő_elrendezés

    def nyomógomb_lenyomva(self, gomb):
        if gomb.text == '=':
            try: self.megoldás.text = str(eval(self.megoldás.text))
            except: pass
        elif gomb.text == 'C':
            self.megoldás.text = ''
        elif gomb.text in self.műveletek and (self.megoldás.text == '' or self.megoldás.text[-1] in self.műveletek):
            return
        else:
            self.megoldás.text = self.megoldás.text + gomb.text

SzámológépApp().run()
