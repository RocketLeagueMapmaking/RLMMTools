import math
import io
from .GUIParameter import GUIParameter


class Protocol():
    """A database comprised of GUIParameters which contains all information about all valid commands"""
    def __init__(self, master=None):
        self.master = master
        self.parameters = {}

        ###############################################
        ###             Meta Parameters             ###
        ###############################################

        self.addParameter(parameter="Asdf")
        self.parameters["Asdf"].permission = 'RW'
        self.parameters["Asdf"].type = 'FLOAT'
        self.parameters["Asdf"].description = 'Testing'
        self.parameters["Asdf"].mode = 'FIX'
        self.parameters["Asdf"].group = 'Test'
        self.parameters["Asdf"].units = '%'
        self.parameters["Asdf"].min = 0
        self.parameters["Asdf"].max = 100
        self.parameters["Asdf"].precision = 3
        self.parameters["Asdf"].scale = 1


    def addParameter(self, parameter="", command="", permission="RW", description="", type="", mode="", group="", units="", min=-math.inf, max=math.inf, precision=0, scale=1):
        self.parameters[parameter] = GUIParameter(parameter, command, permission, description, type, mode, group, units, min, max, precision, scale)
