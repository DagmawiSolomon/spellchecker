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

def get_words(file_path):
    with open (file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
                words = line.split()
                for word_num, word in enumerate(words, start=1):
                    yield line_num, word_num, word
        
    
spellchecker = SpellChecker("words.txt")
for line_num, word_num, word in get_words(filepath):
    suggestions = spellchecker.check(word)
    if suggestions:
        print(f"Misspelled word found at Line {line_num}, Word {word_num}: '{word}'. Possible corrections: {','.join(suggestions)}")
   
    