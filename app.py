# from plugin1.plugin import Plugin
from plugin_framework.plugin_specification import PluginSpecification
from plugin_framework.plugin_manager import *
# from PySide2 import QtWidgets
import sys



plugin_manager = PluginManager()

plugin_manager.install()
print(len(plugin_manager._plugins))

# app = QtWidgets.QApplication(sys.argv)
# mb = QtWidgets.QMessageBox(None, "Upozorenje", "Tekst")
# mb.exec_()
# sys.exit(app.exec_())



