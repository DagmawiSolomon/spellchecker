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
    
    D = [[0]*m]*n
    
    for i in range(n):
        D[i][0] = i
    
    for j in range(m):
        D[0][j] = j
        
    for i in range(1, m):
        for j in range(1, n):
            if str1[i - 1] == str2[j - 1]:
                D[i][j] = D[i - 1][j - 1]
                
            else:
                return 1 + min(D[i - 1][j - 1],  
                                   D[i - 1][j],     
                                   D[i][j - 1])
    return D[m][n]

print(wagner_fischer("Boats", "Float"))