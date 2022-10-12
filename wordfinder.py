from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Create instance of word finder from path of a text file."""
        file = open(path)
        # self.path = path
        self.words = self.get_words_list(file)
        self.report_words_length()

    def __repr__(self):
        """Review representation of word finder instance."""
        return f"<WordFinder path={self.path} words={self.words[:3]}>"

    def get_words_list(self, file):
        """Reads the file, prints out the number of words in file and
        returns a list of words."""
        # file = open(self.path, "r")
        # words = file.read().splitlines()
        # return words
        return [line.strip() for line in file]

    def report_words_length(self):
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the list of words."""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    def get_words_list(self, file):
        return [word for word in super().get_words_list(file)
                if word != "" and not word.startswith("#")]
