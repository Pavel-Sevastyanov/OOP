from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self.version = self.transform(version)

    def __str__(self):
        return '.'.join(self.version)
    
    def __repr__(self):
        return f"Version({repr('.'.join(self.version))})"

    def __eq__(self, other):
        if isinstance(other, Version):
            return tuple(map(int, self.version)) == tuple(map(int, other.version))
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return tuple(map(int, self.version)) < tuple(map(int, other.version))
        return NotImplemented
            
    def transform(self, version):
        version_nums = version.split('.')
        version_nums.extend(['0'] * (3 - len(version_nums)))
        return version_nums
