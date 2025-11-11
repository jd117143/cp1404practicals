"""
CP1404 - Practical 8
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKilometresApp(App):
    """MilesToKilometres is a Kivy App for converting miles to kilometres"""
    output_text = StringProperty()


    def build(self):
        """Build the Kivy App from the .kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation (could be button press or other call), output result to label widget """
        value = self.root.ids.input_number.text
        result = float(value) * 1.6093
        self.output_text = str(result)


MilesToKilometresApp().run()
