class HighScoreTable:
    def __init__(self, max_records):
        self.max_records = max_records
        self._scores = []

    @property
    def scores(self):
        return self._scores[:]

    def update(self, record):
        self._scores.append(record)
        self._scores = sorted(self._scores, reverse=True)[:self.max_records]

    def reset(self):
        self._scores.clear()
