from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain):
        self.chain = chain
        self.base = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
        self.chains = [(elem, self.base[elem]) for elem in self.chain]

    def __getitem__(self, index):
        return self.chains[index]
    
    def __str__(self):
        return f'{self.chain}'

    def __len__(self):
        return len(self.chain)

    def __reversed__(self):
        return reversed(self.chains)

    def __contains__(self, other):
        return other in self.chain

    def __iter__(self):
        yield from self.chains
    
    def __eq__(self, other):
        if isinstance(other, DNA):
            return self.chain == other.chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(self.chain + other.chain)
        return NotImplemented        

