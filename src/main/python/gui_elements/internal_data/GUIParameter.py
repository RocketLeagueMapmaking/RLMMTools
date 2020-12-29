import math
from pyqtsa.SubscriberVariable import SubscriberVariable

MAX_LEN_UNITS = 4
MAX_PRECISION = 8

class GUIParameter(object):
    """A database object which contains all relevant information about a serial parameter as well as a subscriber variable"""
    def __init__(self, parameter="", command="", permission="", description="", type="", mode="", group="", units="", min=-math.inf, max=math.inf, precision=0, scale=1):
        self._parameter = parameter
        self._command = command
        self._permission = permission
        self._description = description
        self._type = type
        self._mode = mode
        self._group = group
        self._units = units
        self._min = min
        self._max = max
        self._precision = precision
        self._scale = scale

        self.variable = SubscriberVariable()
        self.state = None

    # Parameter - the name of the command
    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        self._parameter = parameter
        print(self._parameter)

    @parameter.getter
    def parameter(self):
        return self._parameter

    # Command - the command which is sent
    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command
        print(self._command)

    @command.getter
    def command(self):
        return self._command

    # Permission - read/write/protected to specify command access
    @property
    def permission(self):
        return self._permission

    @permission.setter
    def permission(self, permission):
        self._permission = permission

    @permission.getter
    def permission(self):
        return self._permission

    # Description - a text description of the command
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @description.getter
    def description(self):
        return self._description

    # Type - the data type for the associated variable
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type
        if self.permission.upper() in ['RW', 'WR', 'PRW', 'PWR']:
            if self.type == "BOOL":
                self.min = 0
                self.max = 1
                self.precision = 0
            elif self.type in ["U8", "U16", "U32", "I8", "I16", "I32"]:
                self.precision = 0
            elif self.type in ["FLOAT", "DOUBLE"]:
                self.mode = "FIX"

        elif self.permission.upper() == "R":
            if self.type == "STRING":
                self.variable.value = ""
                return
            else:
                return

    @type.getter
    def type(self):
        return self._type

    # Mode - the textual representation of the variable, e.g. ENUM for a U8
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode
        if self.mode == "ENUM":
            #self.state = SubscriberVariable()
            return

    @mode.getter
    def mode(self):
        return self._mode

    # Group - the functional group of the command
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group

    @group.getter
    def group(self):
        return self._group

    # Units - a string specifying the variable's units
    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, units):
        self._units = units
        if len(self.units) > MAX_LEN_UNITS:
            self._units = self.units[0:MAX_LEN_UNITS]

    @units.getter
    def units(self):
        return self._units

    # Min - the minimum value
    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, min):
        if min <= self.max:
            self._min = min
        else:
            self._min = self.max
        if self.type in ["U8", "U16", "U32", "I8", "I16", "I32"]:
            self._min = int(self.min)

    @min.getter
    def min(self):
        return self._min

    # Max - the maximum value
    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, max):
        if max >= self.min:
            self._max = max
        else:
            self._max = self.min
        if self.type in ["U8", "U16", "U32", "I8", "I16", "I32"]:
            self._max = int(self.max)

    @max.getter
    def max(self):
        return self._max

    # Precision - decimal precision for the variable
    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, precision):
        self._precision = precision
        if self.precision >= 0 :
            if self.precision <= MAX_PRECISION:
                self._precision = precision
            else:
                self._precision = MAX_PRECISION
        else:
            self._precision = 0

    @precision.getter
    def precision(self):
        return self._precision

    # Scale - sets a scale hidden to the user, e.g. user sees 1 but GUI sends 1000000
    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        if self.scale != 0:
            self._scale = scale
            self.min /= self.scale
            self.max /= self.scale

    @scale.getter
    def scale(self):
        return self._scale
