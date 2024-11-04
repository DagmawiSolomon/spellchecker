# Levenshtein distance

def levenshtein_distance(word1, word2):
    if len(word2) == 0:
        return len(word1)
    if len(word1) == 0:
        return len(word2)
    
    li_word1 = list(word1)
    li_word2 = list(word2)
    
    if li_word1[0] == li_word2[0]:
        return levenshtein_distance(word1[1:], word2[1:])
    else:
        return 1 + min(
            levenshtein_distance(word1[1:], word2),
            levenshtein_distance(word1, word2[1:]),
            levenshtein_distance(word1[1:], word2[1:])
        )


print(levenshtein_distance("Dog", "Cog"))