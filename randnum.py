import random

pj=0
pf=0

partie=int(input("Combien de partie(s) voulez-vous jouer ? "))
print("")
for nbr in range(partie):
    parie=int(input("Sur quel chiffre entre 1 et 9 pariez-vous ? "))
    print("")
    alea=random.randint(1, 9)
    if parie==alea:
        print( "tu as parié juste !! Le bon chiffre était : "+str(alea))
        print("")
        pj+=1
            
    else:
        print("Dommage, ce n'est pas le bon chiffre...Le bon chiffre était : "+str( alea))
        print("")
        pf+=1

if pj==partie:
    print("WOW c'est un parfait !! Vous avez parié juste",pj,"fois")
if pf==partie:
    print("C'est quand meme pas de chance !! Vous avez parié faux",pf,"fois")
else:
    print("Vous avez eu",pj,"juste(s) et",pf,"faux.")