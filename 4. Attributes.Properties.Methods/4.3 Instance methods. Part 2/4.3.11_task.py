class TextHandler:
    def __init__(self):
        self.set = []
        
    def add_words(self, text):
        self.set.extend(text.split())
        
    def get_shortest_words(self):
        shortest_lenght = len(min(self.set, key=len, default=''))
        return [el for el in self.set if len(el) == shortest_lenght] 
    
    def get_longest_words(self):
        longest_lenght = len(max(self.set, key=len, default=''))
        return [el for el in self.set if len(el) == longest_lenght]