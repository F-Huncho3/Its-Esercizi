def fibonacci (n:int) -> int : 

    if n <= 0:

        return 0
    
    elif n == 1:

        return 1 
    
    else:

        return int(fibonacci(n-1) + fibonacci(n - 2))
    




def recursiveSum (n:int):

    if n <=0:

        return 0
    
    elif n ==1:

        return 1 
    
    else:

        return n + recursiveSum(n-1)
    

print(recursiveSum())