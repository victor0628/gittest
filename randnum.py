import random

def parier(n):
    alea=random.randint(1, 9)
    if n==alea:
        return "tu as parié juste !! Le bon chiffre était : "+str(alea)
        
    else:
        return "Dommage, ce n'est pas le bon chiffre...Le bon chiffre était : "+str( alea)
    