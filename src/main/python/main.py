from PyQt5 import QtGui, QtWidgets, QtCore
from fbs_runtime.application_context.PyQt5 import ApplicationContext

import sys

from pyqtsa.PyQtSA import *
from pyqtsa.widgetStyles import *

from gui_elements.RLMMTProtocol import RLMMTProtocol

from gui_elements.tabs.Tab_Home import Tab_Home
from gui_elements.tabs.Tab_Boost import Tab_Boost
from gui_elements import _version


class RLMMToolsApp(ApplicationContext):
    def __init__(self):
        super().__init__()

        f = open(self.get_resource("style.css"))
        style = f.read()
        f.close()

        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle(_version.__appname__)
        self.window.setStyleSheet(widgetStyle_mainWindow)

        self.window.setWindowIcon(QtGui.QIcon(self.get_resource('images/logo4_64.ico')))

        self.frame = QtWidgets.QFrame()
        self.window.setCentralWidget(self.frame)

        self.frame.setStyleSheet(widgetStyle_mainWindow)

        width = 1000
        height = 500
        self.window.setGeometry(0, 0, width, height)

        self.layout = QtWidgets.QGridLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.protocol = RLMMTProtocol(master=self)

        self.pages = []
        self.pages.append(Tab_Home(master=self, protocol=self.protocol, index=len(self.pages)))
        self.pages.append(Tab_Boost(master=self, protocol=self.protocol, index=len(self.pages)))


        self.tabs = QSATabWidget(pages=self.pages)
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.configureTab)
        self.tabs.blockSignals(False)
        self.configureTab()

        self.layout.addWidget(self.tabs, 2, 0, 1, 10)

        self.frame.setLayout(self.layout)

        self.window.show()

    def configureTab(self):
        """Update polled loop timers and hidden protected parameters when changing between tabs"""
        self.window.repaint()
        self.tabs.tabBar().setTabButton(self.tabs.index_previous, QTabBar.LeftSide,
                                        self.tabs.pages[self.tabs.index_previous].button_inactive)
        self.tabs.tabBar().setTabButton(self.tabs.currentIndex(), QTabBar.LeftSide,
                                        self.tabs.pages[self.tabs.currentIndex()].button_active)

        self.tabs.index_previous = self.tabs.currentIndex()




if __name__ == "__main__":
    appctxt = ApplicationContext()
    app = RLMMToolsApp()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(_version.__appid__)