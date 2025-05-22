def somma_condizionale(numeri: list[int]) -> int :
    
    sum = 0

    for num in numeri:

        if num %2 == 0 and num %3 ==0:

            sum += num

        else:

            pass

    return sum