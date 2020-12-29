from .internal_data.Protocol import Protocol
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RLMMTProtocol(Protocol):
    """A protocol tailored to the RLMM Tool parameters"""
    def __init__(self, master=None):
        super().__init__(master=master)



        ###############################################
        ###              GUI Parameters             ###
        ###############################################

        self.addParameter(parameter="TESTMESSAGE")
        self.parameters["TESTMESSAGE"].permission = 'R'
        self.parameters["TESTMESSAGE"].type = 'STRING'
        self.parameters["TESTMESSAGE"].group = 'GUI'

        self.addParameter(parameter="TESTRESPONSE")
        self.parameters["TESTRESPONSE"].permission = 'R'
        self.parameters["TESTRESPONSE"].type = 'STRING'
        self.parameters["TESTRESPONSE"].group = 'GUI'

        ###############################################
        ###               Home Parameters           ###
        ###############################################

        self.addParameter(parameter="Test")
        self.parameters["Test"].permission = 'RW'
        self.parameters["Test"].type = 'FLOAT'
        self.parameters["Test"].group = 'HOME'
        self.parameters["Test"].units = '%'
        self.parameters["Test"].min = 0
        self.parameters["Test"].max = 100
        self.parameters["Test"].precision = 1
        self.parameters["Test"].variable.value = 10

