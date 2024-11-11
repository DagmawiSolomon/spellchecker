import time


def execution_time():
    is_evaluating = False
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal is_evaluating
            if is_evaluating:
                return func(*args, **kwargs)
            else:
                start = time.time()
                is_evaluating = True
                try:
                    value = func(*args, **kwargs)
                finally:
                    is_evaluating = False  
                end = time.time()
                print(f"Total execution time for {func.__name__}: {end - start:.8f}s")
                return value
        return wrapper
                
    return decorator

     
def wagner_fischer(str1, str2):
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

print(wagner_fischer("Hate", "Debt"))
