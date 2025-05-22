def sumnumbers(number):
    if number:
        return number + sumnumbers(number-1)
    
    else:
        return 0
    
result = (sumnumbers(10))
print (result)
