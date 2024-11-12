from spellchecker import load_dictionary, wagner_fischer
user_input = input("Enter a word: ")
dictionary = load_dictionary('words.txt')

for word in dictionary:
    if wagner_fischer(user_input, word) == 0:
        print(word)