import re

class CaseHelper:
    def __init__(self):
        pass

    @staticmethod
    def is_snake(text):
        return bool(re.fullmatch(r'([a-z0-9]+_?[a-z0-9]+)+', text))

    @staticmethod
    def is_upper_camel(text):
        return bool(re.fullmatch(r'([A-Z][a-z]*)+', text))        

    @staticmethod
    def to_snake(text):
        text = re.findall(r'([A-Z][a-z]*)', text)
        return '_'.join(word.lower() for word in text)

    @staticmethod
    def to_upper_camel(text):
        return ''.join(word.capitalize() for word in text.split('_'))