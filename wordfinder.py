import doctest
import random


class WordFinder:
    def __init__(self, file_path):
        self.words = self.read_words(file_path)
        print(f"{len(self.words)} words read")

    def read_words(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def read_words(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]


if __name__ == "__main__":
    wf = WordFinder("words.txt")

    random_word = wf.random()
    print(f"Random word: {random_word}")

    swf = SpecialWordFinder("words.txt")

    random_special_word = swf.random()
    print(f"Random special word: {random_special_word}")


def run_tests():
    """
    >>> wf = WordFinder("words.txt")
    {} words read
    >>> len(wf.words) == {}
    True
    >>> word = wf.random()
    >>> word in wf.words
    True
    """.format(len(wf.words), len(wf.words))
    pass


if __name__ == "__main__":
    run_tests()
