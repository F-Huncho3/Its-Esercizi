def even_odd_pattern(numbers:list[int]) -> list[int]:
    
    i = 0

    new_list = []

    for number in numbers:

        if number%2 == 0:

            new_list.append(number)

        else:

            pass

    for number in numbers:

        if number%2 != 0:

            new_list.append(number)

    return new_list





