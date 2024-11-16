import argparse
from spellchecker import SpellChecker

parser = argparse.ArgumentParser(
                    prog='SpellChecker',
                    description='A simple python spell checker',
)

parser.add_argument(
        "filepath",
        type=str,
        help="The path to the file."
)

args = parser.parse_args()
filepath = args.filepath

words = []
with open (filepath, 'r') as file:
    words = file.read().split()
    
spellchecker = SpellChecker("words.txt")
for i, word in enumerate(words):
    print(f"{word}: {spellchecker.check(word)}")
    
    