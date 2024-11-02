from copy import deepcopy

class SequenceZip:
    def __init__(self, *args):
        self.sequences = args
        self.tuple_sequences = list(zip(*deepcopy(self.sequences)))
        
    def __len__(self):
        return len(self.tuple_sequences)
    
    def __iter__(self):
        yield from self.tuple_sequences
        
    def __getitem__(self, index):
        return self.tuple_sequences[index]