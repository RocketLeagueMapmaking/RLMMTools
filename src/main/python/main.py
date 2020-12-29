from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

class RLMMToolsApp(ApplicationContext):
    def __init__(self):
        super().__init__()




if __name__ == '__main__':
    appctxt = RLMMToolsApp()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)