def calcola_stipendio(ore_lavorate: int) -> float:
    
    if ore_lavorate <= 40:

        stipendiolordo = ore_lavorate*10

        return stipendiolordo
    
    elif ore_lavorate > 40:

        oreExtra = ore_lavorate - 40

        stipendiolordo = (oreExtra*15) + 400

        return stipendiolordo