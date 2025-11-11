"""
CP1404 - Practical 8
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometresApp(App):
    """MilesToKilometres is a Kivy App for converting miles to kilometres"""
    message = StringProperty()

    def build(self):
        """Build the Kivy App from the .kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        self.message = self.root.ids.input_number.text


MilesToKilometresApp().run()
