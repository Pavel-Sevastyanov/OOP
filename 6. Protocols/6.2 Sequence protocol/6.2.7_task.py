from collections import defaultdict

class HistoryDict:
    def __init__(self, data=None):
        self.data = {} if data is None else dict(data)
        self._history = defaultdict(list)
        for k, v in self.data.items():
            self._history[k].append(v)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def history(self, key):
        if key in self._history:
            return self._history[key]
        else:
            return []

    def all_history(self):
        return dict(self._history)

    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        yield from self.data

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self._history[key].append(value)

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
            del self._history[key]
