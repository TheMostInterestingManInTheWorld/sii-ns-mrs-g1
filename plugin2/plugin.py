from plugin_interface import PluginInterface
from plugin_specification import PluginSpecification

class Plugin(PluginInterface):
    def __init__(self, plugin_specification):
        super().__init__()
        self._plugin_specification = plugin_specification

    def activate(self):
        print("Hello everyone")
    
    def deactivate(self):
        print("Goodbye everyone")

