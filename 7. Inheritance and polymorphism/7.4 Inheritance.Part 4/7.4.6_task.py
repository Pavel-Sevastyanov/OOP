class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        return

    def keys_of(self, value):
        values = [k for k, v in self.items() if v == value]
        return values