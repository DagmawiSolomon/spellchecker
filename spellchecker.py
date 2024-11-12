
class SpellChecker:
    def wagner_fischer(str1: str, str2: str) -> int:
        """Calculates the Levenshtein edit distance between two strings using the Wagner-Fischer algorithm.
        
        The Levenshtein distance is a metric for measuring the difference between two sequences. 
        It represents the minimum number of single-character edits (insertions, deletions, or substitutions) 
        required to transform one string into the other.
        
        Args:
            str1 (str): The first input string.
            str2 (str): The second input string.
        
        Returns:
            int: The edit distance between the two strings, indicating the minimum number of edits needed.
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


    def load_dictionary(filepath: str) -> list:
        """Loads words from a dictionary file and returns them as a list.
        
        Args:
            filepath (str): The path to the dictionary file containing words, one per line.
        
        Returns:
            list: A list of words from the dictionary file.
        """
        with open(filepath, 'r') as file:
            dictionary = file.read().splitlines()
        return dictionary