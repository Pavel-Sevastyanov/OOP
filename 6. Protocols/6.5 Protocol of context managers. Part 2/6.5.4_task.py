class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'rt', encoding='utf-8')
        return map(str.strip, self.file.readlines())

    def __exit__(self, *args, **kwargs):
        self.file.close()