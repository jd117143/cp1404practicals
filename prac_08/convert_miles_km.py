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
        """Handle calculation (could be button press or other call), output result to label widget."""
        value = self.get_valid_number()
        result = value * 1.6093
        self.output_text = str(result)

    def handle_increment(self, increment):
        """Handle up/down button press, update text input."""
        value = self.get_valid_number() + increment
        self.root.ids.input_number.text = str(value)

    def get_valid_number(self):
        """Get text input value, return as a float if valid and 0.0 if invalid."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


MilesToKilometresApp().run()
