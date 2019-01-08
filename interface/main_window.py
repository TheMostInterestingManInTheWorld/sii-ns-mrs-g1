from PySide2 import QtWidgets, QtGui
from interface.dialogs.plugins_dialog import PluginsDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, plugin_manager=None):
        super().__init__(parent)
        self.setWindowTitle("Nasa aplikacija")
        self.setWindowIcon(QtGui.QIcon("resources/icons/application.png"))
        self.resize(800, 600)

        self.plugin_manager = plugin_manager

        # kreiranje menija i toolbarova
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.toolbar = QtWidgets.QToolBar("Toolbar", self)
        self.central_widget = QtWidgets.QTextEdit(self)
        self.actions_dict = {
            "new": QtWidgets.QAction(QtGui.QIcon("resources/icons/document.png"), "&New", self),
            "plugins": QtWidgets.QAction(QtGui.QIcon("resources/icons/puzzle.png"), "&Plugin settings", self)
        }
        # populisemo menije
        self._populate_menu_bar()
        # populisemo toolbarove
        self._populate_toolbar()
        # uvezivanje akcija
        self.setCentralWidget(self.central_widget)
        self._bind_actions()
        
    
    def _populate_menu_bar(self):
        file_menu = QtWidgets.QMenu("&File")
        view_menu = QtWidgets.QMenu("&View")
        # uvezemo akcije
        file_menu.addAction(self.actions_dict["new"])
        file_menu.addAction(self.actions_dict["plugins"])
        view_menu.addAction(self.toolbar.toggleViewAction())

        self.menu_bar.addMenu(file_menu)
        self.menu_bar.addMenu(view_menu)
        self.setMenuBar(self.menu_bar)

    def _populate_toolbar(self):
        # uvezemo akcije
        self.toolbar.addAction(self.actions_dict["new"])
        self.addToolBar(self.toolbar)

    def _bind_actions(self):
        self.actions_dict["new"].setShortcut("Ctrl+N")
        self.actions_dict["plugins"].setShortcut("Ctrl+P")
        self.actions_dict["new"].triggered.connect(self._on_new_file)
        self.actions_dict["plugins"].triggered.connect(self._on_plugin_settings)

    def _on_new_file(self):
        # file_dialog = QtWidgets.QFileDialog(self, "New file", ".", "Python files (*.py)")
        # file_dialog.exec_()
        # print(file_dialog.selectedFiles())
        print(self.central_widget.toPlainText())

    def _on_plugin_settings(self):
        PluginsDialog(self, self.plugin_manager).exec_()

    def set_central_widget(self, widget, toolbar=None, menu=None):
        # FIXME: prepraviti da se ovde prosledjuje samo string symbolic_name, a na osnovu toga se odabere plugin i kreira widget
        self.setCentralWidget(widget)
        self.toolbar.addActions(toolbar.actions()) if toolbar is not None else None
        self.menu_bar.addMenu(menu) if menu is not None else None



