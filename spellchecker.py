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

     

# Levenshtein distance
@execution_time()
def levenshtein_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    
     
    if word1[0] ==word2[0]:
        return levenshtein_distance(word1[1:], word2[1:])
    else:
        return 1 + min(
            levenshtein_distance(word1[1:], word2),
            levenshtein_distance(word1, word2[1:]),
            levenshtein_distance(word1[1:], word2[1:])
        )


print(levenshtein_distance("Dog", "Cat"))