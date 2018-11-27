import json
import os
from plugin_framework.plugin_specification import PluginSpecification
from importlib import import_module
from inspect import getmembers, isclass

class PluginManager:
    def __init__(self):
        self._plugins = []

    def activate(self, plugin):
        plugin.activate()
        self._plugins.append(plugin)

    def deactivate(self, plugin):
        plugin.deactivate()
        self._plugins.remove(plugin)

    
    def install(self, path="plugins"):
        for d in os.scandir(path):
            if d.is_dir() and (d.name != "__pycache__"):
                package_path = os.path.join(path, d.name)
                plugin_path = os.path.join(package_path, "plugin.py")
                spec_path = os.path.join(package_path, "spec.json")
                with open(spec_path, "r") as fp:
                    spec = json.load(fp)
                    plugin_module = import_module(plugin_path.replace(os.path.sep, ".").rstrip(".py"))
                    class_members = getmembers(plugin_path, isclass)
                    if len(class_members) == 1:
                        plugin = plugin_module.Plugin(PluginSpecification(spec))
                        self.activate(plugin)

    def uninstall(self, plugin):
        # deaktivirati plugin
        # izmenimo specifikaciju konfiguracione datoteke da je plugin obrisan
        self.deactivate(plugin)
    

        
