import string


class StrExtension:
    def __init__(self):
        pass

    @staticmethod
    def remove_vowels(text):
        text = filter(lambda c: c not in 'aeiouyAEIOUY', text)
        return ''.join(text)

    @staticmethod
    def leave_alpha(text):
        text = filter(lambda c: c in string.ascii_letters, text)
        return ''.join(text)

    @staticmethod
    def replace_all(text, chars, char):
        text = map(lambda c: char if c in chars else c, text)
        return ''.join(text)
