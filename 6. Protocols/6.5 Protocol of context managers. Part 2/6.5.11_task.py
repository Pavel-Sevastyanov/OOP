class HtmlTag:
    level = -1    
    def __init__(self, tag, inline=False):
        self.open_tag = '<' + tag + '>'
        self.close_tag = '</' + tag + '>'
        self.inline = inline
        self.level = 0

    def __enter__(self):
        __class__.level +=1
        print('  ' * __class__.level + self.open_tag, end='' if self.inline else '\n')
        return self

    def __exit__(self, *args, **kwargs):
        if not self.inline:
            self.level = __class__.level
        print('  ' * self.level + self.close_tag)
        __class__.level -=1

    def print(self, text):
        if not self.inline:
            self.level = __class__.level + 1
        print('  ' * self.level, text, sep='', end='' if self.inline else '\n')