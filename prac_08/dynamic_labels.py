"""
CP1404 - Practical 8
Kivy GUI program to create dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to create dynamic labels."""

    def __init__(self, **kwargs):
        """Construct main Kivy App."""
        super().__init__(**kwargs)
        self.name = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy App from the .kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


DynamicLabelsApp().run()
