class Wordplay:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)
    
    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        return list(filter(lambda word: all(map(lambda let: let in args, word)), self.words))
    
    def avoid(self, *args):
        return list(filter(lambda word: all(map(lambda let: let not in word, args)), self.words))