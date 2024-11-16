from collections import UserDict

class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        for k, v in self.items():
            if v == value:
                print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
                break
        self.data.__setitem__(key, value)