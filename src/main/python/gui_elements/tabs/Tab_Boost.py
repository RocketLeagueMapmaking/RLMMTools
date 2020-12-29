from pyqtsa.PyQtSA import *
from pyqtsa.widgetStyles import *

import pyperclip

import datetime

class Tab_Boost(QSATab):
    def __init__(self, master=None, protocol=None, index=0):
        super().__init__(master=master, protocol=protocol,
                         title="Boost",
                         icon="images/boost_24.png",
                         index=index,
                         widgets=[Cluster_CopyBoost(master=self, protocol=protocol)
                                  ]
                         )
        self.button_active.setContextMenuPolicy(Qt.PreventContextMenu)


class Button_CopyBoostPad(QSAPushbutton):
    def __init__(self, master=None, protocol=None):
        super().__init__(master=master,
                         parameter=protocol.parameters["Test"],
                         text="Boost Pad"
                         )

    def onClick(self):
        f = open(self.master.master.master.get_resource("textblock\\boostpad.txt"))
        text = f.read()
        f.close()
        pyperclip.copy(text)

class Button_CopyBoostPill(QSAPushbutton):
    def __init__(self, master=None, protocol=None):
        super().__init__(master=master,
                         parameter=protocol.parameters["Test"],
                         text="Boost Pill",
                         )

    def onClick(self):
        command = 'echo ' + "testing2" + '| clip'
        os.system(command)

class Cluster_CopyBoost(QSAWidgetCluster):
    def __init__(self, master=None, protocol=None):
        super().__init__(master=master,
                         text="Copy to Clipboard",
                         widgets=[Button_CopyBoostPad(master=self, protocol=protocol),
                                  Button_CopyBoostPill(master=self, protocol=protocol),
                         ]
                         )