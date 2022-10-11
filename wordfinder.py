from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create instance of word finder from path of a text file."""
        self.path = path
        self.words = self.read_file()

    def __repr__(self):
        """Review representation of word finder instance."""
        return f"<WordFinder path={self.path} words={self.words[:3]}>"

    def read_file(self):
        """Reads the file, prints out the number of words in file and
        returns a list of words."""
        file = open(self.path, "r")
        words = file.read().splitlines()
        print(f"{len(words)} words read")
        return words

    def random(self):
        """Returns a random word from the list of words."""
        return choice(self.words)


    # Subclass, split things differently (some refactoring)
