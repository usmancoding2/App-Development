def square(n):
    if n < 1 or n > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        for i in range(1,65):
            return 2 **(n-1)
    
    
    
    


def total():
    a = []
    for n in range(1, 65):
        squared_value = 2 ** (n - 1)
        a.append(squared_value)
    return sum(a)   
