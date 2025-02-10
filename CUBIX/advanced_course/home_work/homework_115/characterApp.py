from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
import sqlite3

class CharacterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_path = "characters.db"
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY, 
                name TEXT UNIQUE, 
                strength INTEGER, 
                agility INTEGER, 
                hp INTEGER
            )
        """)
        self.conn.commit()
        self.selected_character = None

    def build(self):
        Window.clearcolor = (0.1, 0.3, 0.1, 1)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.character_spinner = Spinner(text="Select Character", size_hint_y=None, height=35)
        self.character_spinner.bind(text=self.load_character)

        self.name_input = TextInput(hint_text='Character Name', multiline=False, size_hint_y=None, height=35)
        self.strength_input = TextInput(hint_text='Strength', input_filter='int', multiline=False, size_hint_y=None, height=35)
        self.agility_input = TextInput(hint_text='Agility', input_filter='int', multiline=False, size_hint_y=None, height=35)
        self.hp_input = TextInput(hint_text='HP', input_filter='int', multiline=False, size_hint_y=None, height=35)

        self.add_button = Button(text='Add Character', on_press=self.add_character, background_color=(0.1, 0.7, 0.1, 1), size_hint_y=None, height=40)
        self.update_button = Button(text='Update Character', on_press=self.update_character, background_color=(0.7, 0.5, 0.1, 1), size_hint_y=None, height=40)
        self.view_button = Button(text='View Characters', on_press=self.view_characters, background_color=(0.1, 0.7, 0.1, 1), size_hint_y=None, height=40)

        self.result_label = Label(text='', size_hint_y=None, height=30)

        self.scroll_layout = ScrollView(size_hint=(1, None), height=200)
        self.character_label = Label(text='', size_hint_y=None, height=1000)
        self.scroll_layout.add_widget(self.character_label)

        self.layout.add_widget(Label(text='Select Character to Edit', color=(1, 1, 1, 1)))
        self.layout.add_widget(self.character_spinner)
        self.layout.add_widget(Label(text='Enter Character Stats', color=(1, 1, 1, 1)))
        self.layout.add_widget(self.name_input)
        self.layout.add_widget(self.strength_input)
        self.layout.add_widget(self.agility_input)
        self.layout.add_widget(self.hp_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.update_button)
        self.layout.add_widget(self.view_button)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.scroll_layout)

        self.load_character_list()

        return self.layout

    def add_character(self, instance):
        name = self.name_input.text
        strength = self.strength_input.text
        agility = self.agility_input.text
        hp = self.hp_input.text

        if name and strength and agility and hp:
            try:
                self.cursor.execute("INSERT INTO characters (name, strength, agility, hp) VALUES (?, ?, ?, ?)",
                                    (name, int(strength), int(agility), int(hp)))
                self.conn.commit()
                self.result_label.text = f'Added {name}!'
                self.load_character_list()
            except sqlite3.IntegrityError:
                self.result_label.text = 'Character name must be unique!'
        else:
            self.result_label.text = 'Fill in all fields!'

        self.clear_inputs()

    def view_characters(self, instance):
        self.cursor.execute("SELECT * FROM characters")
        characters = self.cursor.fetchall()
        if characters:
            self.character_label.text = '\n'.join([f'{char[1]} - STR: {char[2]}, AGI: {char[3]}, HP: {char[4]}' for char in characters])
        else:
            self.character_label.text = 'No characters found.'

    def load_character_list(self):
        self.cursor.execute("SELECT name FROM characters")
        characters = self.cursor.fetchall()
        if characters:
            self.character_spinner.values = [char[0] for char in characters]
        else:
            self.character_spinner.values = ["No Characters"]

    def load_character(self, spinner, text):
        if text == "No Characters":
            return

        self.cursor.execute("SELECT * FROM characters WHERE name = ?", (text,))
        character = self.cursor.fetchone()

        if character:
            self.selected_character = character[0]
            self.name_input.text = character[1]
            self.strength_input.text = str(character[2])
            self.agility_input.text = str(character[3])
            self.hp_input.text = str(character[4])

    def update_character(self, instance):
        if not self.selected_character:
            self.result_label.text = "Select a character to update!"
            return

        name = self.name_input.text
        strength = self.strength_input.text
        agility = self.agility_input.text
        hp = self.hp_input.text

        if name and strength and agility and hp:
            self.cursor.execute("UPDATE characters SET name=?, strength=?, agility=?, hp=? WHERE id=?",
                                (name, int(strength), int(agility), int(hp), self.selected_character))
            self.conn.commit()
            self.result_label.text = f'{name} updated successfully!'
            self.load_character_list()
        else:
            self.result_label.text = 'Fill in all fields!'

        self.clear_inputs()

    def clear_inputs(self):
        self.name_input.text = ''
        self.strength_input.text = ''
        self.agility_input.text = ''
        self.hp_input.text = ''
        self.selected_character = None
        self.character_spinner.text = "Select Character"

    def on_stop(self):
        self.conn.close() 

if __name__ == '__main__':
    CharacterApp().run()
