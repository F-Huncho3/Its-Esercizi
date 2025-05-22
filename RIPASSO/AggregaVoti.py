def aggrega_voti(voti: list[dict]) -> dict[str, list[int]]:
    new_dict: dict[str, list[int]] = {}

    for voto in voti:
        nome = voto["nome"]
        punteggio = voto["voto"]
        
        if nome not in new_dict:
            new_dict[nome] = []
        new_dict[nome].append(punteggio)
    
    return new_dict


