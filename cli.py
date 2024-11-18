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
            "--file",
            type=str,
            help = "Specify a file"
        )
        
        parser.add_argument(
            "--word",
            type=str,
            help = "Specify a word"
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

    def check_file(self, filepath):
        """Checks spelling in the provided file and suggests corrections."""
        for line_num, word_num, word in self.get_words(filepath):
            suggestions = self.spellchecker.check(word)
            if suggestions:
                print(f"Misspelled word found at Line {line_num}, Word {word_num}: '{word}'. "
                      f"Possible corrections: {', '.join(suggestions)}")
                
    def check_word(self, word):
        """Checks spelling of the provided word and suggests corrections."""
        suggestions = self.spellchecker.check(word)
        if suggestions:
            print(f"Possible corrections for the word '{word}': {', '.join(suggestions)}")
        else:
            print(f"The word '{word}' appears to be spelled correctly.")
        
        

    def run(self):
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
