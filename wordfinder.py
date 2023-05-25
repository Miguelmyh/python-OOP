"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, path):
        self.path = open(path, "r")
        self.words = self.read()
        print("there is ", len(self.words), "words")

    def random(self):
        return

    def read(self):
        value = self.path.read().splitlines()
        return value

    def random(self):
        value = random.choice(self.words)
        return value


class SpecialWordFinder(WordFinder):
    def read(self):
        return [w.strip() for w in self.path if w.strip() and not w.startswith("#")]
