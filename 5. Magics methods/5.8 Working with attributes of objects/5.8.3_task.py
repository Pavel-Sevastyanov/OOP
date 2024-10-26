class Ord:
    def __init__(self):
        pass

    def __getattr__(self, char):
        return ord(char)