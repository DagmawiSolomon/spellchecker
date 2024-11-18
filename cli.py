import argparse
from spellchecker import SpellChecker


class SpellCheckerApp:
    def __init__(self, dictionary_path):
        self.spellchecker = SpellChecker(dictionary_path)

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            prog='SpellChecker',
            description='A simple python spell checker',
        )
        parser.add_argument(
            "filepath",
            type=str,
            help="The path to the file."
        )
        return parser.parse_args()

    @staticmethod
    def get_words(file_path):
        """Generator to yield words from the file along with their positions."""
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                words = line.split()
                for word_num, word in enumerate(words, start=1):
                    yield line_num, word_num, word

    def check_spelling(self, filepath):
        """Checks spelling in the provided file and suggests corrections."""
        for line_num, word_num, word in self.get_words(filepath):
            suggestions = self.spellchecker.check(word)
            if suggestions:
                print(f"Misspelled word found at Line {line_num}, Word {word_num}: '{word}'. "
                      f"Possible corrections: {', '.join(suggestions)}")

    def run(self):
        args = self.parse_arguments()
        self.check_spelling(args.filepath)


if __name__ == "__main__":
    app = SpellCheckerApp(dictionary_path="words.txt")
    app.run()
