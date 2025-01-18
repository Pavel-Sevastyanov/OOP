from collections import defaultdict
from math import ceil


class Pagination:
    def __init__(self, sequence, size):
        self.sequence = sequence
        self.size = size
        self.total_pages = ceil(len(self.sequence) / size)
        self.book = {}
        self.current_page = 1
        self.create_book()

    def create_book(self):
        start, end = 0, self.size       

        for page in range(1, self.total_pages + 1):
            self.book[page] = self.sequence[start:end]
            start, end = end, end + self.size

    def get_visible_items(self):
        return self.book[self.current_page]

    def prev_page(self):
        if self.current_page != 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page != self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, number):
        if number < 1:
            self.current_page = 1
        elif number > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = number
        return self
