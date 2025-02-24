N:int = int(input("Inserisci un euro per ogni barretta che vuoi acquistare (ogni barretta acquistata vale come buono e con 6 buoni ne riceverai una gratis )"))

buoni_sconto = 0

barrette_totali = 0 

barrette_gratis = 0

barrette_acquistate = 0 

if N > 0:

    barrette_acquistate += N 
    
    buoni_sconto += N
    
    while buoni_sconto >= 6:

        buoni_sconto -= 6

        barrette_gratis +=1 

        barrette_totali = barrette_gratis +  barrette_acquistate
        
        print (f"I buoni disponibili sono {buoni_sconto} e hai reclamato una barretta gratis")
        

print (f"Hai acquistato {barrette_totali} barrette di cui {barrette_gratis} tramite buoni sconto") 



