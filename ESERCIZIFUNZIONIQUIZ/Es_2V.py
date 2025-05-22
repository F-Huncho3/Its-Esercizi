def blackjack_hand_total(cards: list[int]) -> int:
    

    value = 0

    for i in cards:

        value+= i

        if value > 21:

            for i in cards:

                if i == 11:

                    value -=10
                else:

                    pass

            
    return value

blackjack_hand_total([2,3,5])