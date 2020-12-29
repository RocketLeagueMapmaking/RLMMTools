from pyqtsa.PyQtSA import *
from pyqtsa.widgetStyles import *

import datetime

class Tab_Home(QSATab):
    def __init__(self, master=None, protocol=None, index=0):
        super().__init__(master=master, protocol=protocol,
                         title="Home",
                         icon="images/logo4_24.png",
                         index=index,
                         widgets=[Cluster_Test(master=self, protocol=protocol)]
                         )
        self.button_active.setContextMenuPolicy(Qt.PreventContextMenu)


class Readout_Test(QSAInfoFrame):
    def __init__(self, master=None, protocol=None):
        super().__init__(master=master,
                         parameter=protocol.parameters["Test"],
                         text="Test",
                         interval=1
                         )


class Cluster_Test(QSAWidgetCluster):
    def __init__(self, master=None, protocol=None):
        super().__init__(master=master,
                         text="Test",
                         widgets=[Readout_Test(master=self, protocol=protocol)
                         ]
                         )