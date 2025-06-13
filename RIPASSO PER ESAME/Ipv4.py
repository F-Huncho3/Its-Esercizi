def is_valid_ipv4(ip: str) -> bool:
    
    parti = ip.split('.')
    
    
    if len(parti) != 4:
        
        return False
    
    for parte in parti:
        
        if not parte.isdigit() == True:
            
            return False
       
        numero = int(parte)
        
        if numero < 0 or numero > 255:
            
            return False
    
    return True