from plugin_framework.plugin import Plugin
from PySide2 import QtWidgets

class Main(Plugin):
    def __init__(self, plugin_specification):
        super().__init__(plugin_specification)

    def activate(self):
        print("Hello everyone")
    
    def deactivate(self):
        print("Goodbye everyone")

    def get_widget(self, parent=None):
        return QtWidgets.QTextEdit(parent), None, None

