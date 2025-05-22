def integerPower (base:int,esponente:int) -> int:
    esponentialnumb= 0
    
    for i in range(esponente+1):

        esponentialnumb += base*base

    return esponentialnumb
