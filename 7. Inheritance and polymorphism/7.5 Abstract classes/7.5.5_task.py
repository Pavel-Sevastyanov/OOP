from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args):
        self.seq = []
        for elem in args:
            if isinstance(elem, int):
                self.seq.append(elem)
            else:
                start, end = map(int, elem.split('-'))
                for num in range(start, end + 1):
                    self.seq.append(num)
        
    def __getitem__(self, index):
        return self.seq[index]

    def __len__(self):
        return len(self.seq)

    def __reversed__(self):
        return reversed(self.seq)
