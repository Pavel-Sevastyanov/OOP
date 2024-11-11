class User:
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return False


class PremiumUser(User):
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return True