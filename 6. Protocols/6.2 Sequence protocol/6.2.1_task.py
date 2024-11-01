class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        yield from reversed(self.sequence) 

    def __getitem__(self, index):
        return self.sequence[~index]