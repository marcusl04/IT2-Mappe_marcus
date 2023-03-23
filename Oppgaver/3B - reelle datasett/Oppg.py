1. 
# Ser forskjell, æ, ø og å vises ikke.

2. 
filnavn = "MikkelRev.txt"
linjeliste = []
with open(filnavn, encoding="utf-8") as fil:
 for linje in fil:
    linjeliste.append(linje)
print(linjeliste)