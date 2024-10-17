class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexc):
        self.r = int(hexc[:2], 16)
        self.g = int(hexc[2:4], 16)
        self.b = int(hexc[4:], 16)
        self._hexcode = hexc