class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *args):
        self.juniors.extend(list(args))

    def add_senior(self, *args):
        self.seniors.extend(list(args))

    def __iter__(self):
        for dev in self.juniors:
            yield dev, 'junior'

        for dev in self.seniors:
            yield dev, 'senior'
