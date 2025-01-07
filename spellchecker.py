
class SpellChecker:

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = self.load_dictionary(filepath)
        
    def wagner_fischer(self, str1: str, str2: str) -> int:

        """
        Calculates the Levenshtein edit distance between two strings
        using the Wagner-Fischer algorithm.

        The Levenshtein distance is a metric for measuring the
        difference between two sequences.
        It represents the minimum number of single-character edits
        (insertions, deletions, or substitutions)
        required to transform one string into the other.

        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            int: The edit distance between the two strings,
            indicating the minimum number of edits needed.
        """
        m, n = len(str1), len(str2)

        # Initialize a 2D array with dimensions (n+1) x (m+1) for storing edit distances
        D = [[0] * (m+1) for _ in range(n+1)]

        # Initialize the first column of the array (edit distance from str1 to an empty str2)
        for i in range(n+1):
            D[i][0] = i

        # Initialize the first row of the array (edit distance from an empty str1 to str2)
        for j in range(m+1):
            D[0][j] = j
            
        # Fill in the rest of the matrix
        for i in range(1, n+1):
            for j in range(1, m+1):
                # Check if the characters from both strings are the same
                if str1[j-1] == str2[i-1]:
                    D[i][j] = D[i-1][j-1]                
                else:
                    # Get the minimum of the three possible operations (substitute, remove, insert)
                    D[i][j] = 1 + min(D[i - 1][j - 1],  # Substitute
                                    D[i - 1][j],     # Remove
                                    D[i][j - 1])     # Insert
        return D[n][m]
    
    def check(self, input_word: str) -> list:
        """
        Checks if a given word is present in the dictionary or finds close matches 
        using the Wagner-Fischer algorithm. Returns words with an edit distance of 1 
        from the input word.

        Args:
            input_word (str): The word to check against the dictionary.

        Returns:
            list: A list of recommended words from the dictionary that have an 
                edit distance of 1 from the input word. If the exact word is found 
                (edit distance 0), an empty list is returned. If no close matches 
                are found, the list will be empty.
        """
        recommendations = []
        for dictionary_word in self.words:
            edit_distance = self.wagner_fischer(input_word.lower(), dictionary_word)
            if edit_distance == 0:
                return []  
            elif edit_distance == 1:
                recommendations.append(dictionary_word) 

        return recommendations 
    
        
    def load_dictionary(self, filepath: str) -> list:
        """Loads words from a dictionary file and returns them as a list.
        
        Args:
            filepath (str): The path to the dictionary file containing words, one per line.
        
        Returns:
            list: A list of words from the dictionary file.
        """
        dictionary = []
        with open(filepath, 'r') as file:
            dictionary = file.read().splitlines()
        return dictionary