import sys

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

lst_bs = [BookStudy(i.split(';')[0], i.split(';')[1], i.split(';')[2]) for i in lst_in]
unique_books = len(set(lst_bs))