class Testpaper:
    def __init__(self, theme, test_answers, percent):
        self.theme = theme
        self.test_answers = test_answers
        self.percent = percent


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test, students_answers):
        if isinstance(self.tests_taken,  str):
            self.tests_taken = {}
        correct_answers = len(list(filter(lambda tup: tup[0] == tup[1], zip(test.test_answers, students_answers))))
        correct_percent = round(correct_answers * 100 / len(test.test_answers))
        result = ['Failed!', 'Passed!'][correct_percent >= int(test.percent[:-1])]
        self.tests_taken[test.theme] = f'{result} ({correct_percent}%)'
