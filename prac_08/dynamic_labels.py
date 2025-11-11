"""
CP1404 - Practical 8
Kivy GUI program to create dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to create dynamic labels."""

    def build(self):
        """Build the Kivy App from the .kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


DynamicLabelsApp().run()
