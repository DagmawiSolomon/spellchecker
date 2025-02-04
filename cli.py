import argparse
from typing import Iterator, Tuple
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
            "--file",
            type=str,
            help="Specify a file"
        )
        parser.add_argument(
            "--word",
            type=str,
            help="Specify a word"
        )
        return parser.parse_args()

    @staticmethod
    def get_words(file_path: str) -> Iterator[Tuple[int, int, str]]:
        """
        Generator to yield words from the file along with their positions.
        Args:
            filepath (str): The path to the file.
        Yields:
            Tuple[int, int, str]: A tuple containing:
            - The line number (1-based index) where the word is found.
            - The word number (1-based index) in that line.
            - The word itself.
        """
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                words = line.split()
                for word_num, word in enumerate(words, start=1):
                    yield line_num, word_num, word

    def check_file(self: "SpellCheckerApp", filepath: str) -> None:
        """
        Checks spelling in the provided file and suggests corrections.
        Args:
        filepath (str): The path to the file to be checked for spelling errors.
        Returns:
        None: prints the misspelled words and suggestions directly.

        """
        for line_num, word_num, word in self.get_words(filepath):
            suggestions = self.spellchecker.check(word)
            if suggestions:
                print(f"{filepath}:{line_num}:{word_num}: "
                      f"Possible corrections: {', '.join(suggestions)}"
                      )
    
    def check_word(self: "SpellCheckerApp", word: str) -> None:
        """
        Checks spelling of the provided word and suggests corrections.
        Args:
        filepath (str): The path to the file to be checked for spelling errors.

        Returns:
        None: prints the misspelled words and suggestions directly.
        """
        suggestions = self.spellchecker.check(word)
        if suggestions:
            print(
                f"Possible corrections for the word '{word}': "
                f"{', '.join(suggestions)}")
        else:
            print(f"The word '{word}' appears to be spelled correctly.")
    
    def run(self: "SpellCheckerApp") -> None:
        args = self.parse_arguments()
        if args.file:
            self.check_file(args.file)
        elif args.word:
            self.check_word(args.word)
        else:
            print("You must specify either a file or a word to spell check")
           

if __name__ == "__main__":
    app = SpellCheckerApp(dictionary_path="words.txt")
    app.run()
