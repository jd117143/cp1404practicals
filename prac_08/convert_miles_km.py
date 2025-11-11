"""
CP1404 - Practical 8
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


class MilesToKilometresApp(App):
    """MilesToKilometres is a Kivy App for converting miles to kilometres"""

    def build(self):
        """Build the Kivy App from the .kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKilometresApp().run()
