def transform(x: int) -> int:
    
    if x%2 == 0:

        newX = x/2

        return newX
    
    elif x%2 != 0:

        newX = (x*3)-1

        return newX