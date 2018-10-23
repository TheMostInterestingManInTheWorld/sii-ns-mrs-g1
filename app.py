from plugin1.plugin import Plugin
from plugin_specification import PluginSpecification
from plugin_manager import *



plugin_manager = PluginManager()

plugin_manager.install()
print(len(plugin_manager._plugins))
plugin_manager.uninstall(plugin_manager._plugins[0])
plugin_manager.uninstall(plugin_manager._plugins[0])
