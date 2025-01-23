import copy

class Selfie:
    def __init__(self):
        self.states = {}
        self._n_states = 0

    def save_state(self):
        self.states[self._n_states] = copy.deepcopy(self)
        self._n_states += 1
    
    def recover_state(self, index):
        if index in self.states:
           self.__dict__ = self.states[index].__dict__
        return self

    def n_states(self):
        return self._n_states

