from plugin_framework.plugin import Plugin
from PySide2 import QtWebEngineWidgets

class Main(Plugin):
    def __init__(self, plugin_specification):
        super().__init__(plugin_specification)

    def activate(self):
        print("Hello world")
    
    def deactivate(self):
        print("Goodbye")

    def get_widget(self, parent=None):
        return QtWebEngineWidgets.QWebEngineView(parent), None, None


