# Arv
Arv i Python handler om å lage nye klasser basert på eksisterende klasser.
Tenk på klasser som forskjellige typer ting (f.eks. biler eller dyr).
Når vi arver fra en eksisterende klasse, kan vi ta med oss alle egenskapene og metodene til den klassen, og deretter legge til eller endre dem for å lage en ny klasse som er mer spesifikk.
For eksempel kan vi arve fra en generell klasse for biler og deretter lage en mer spesifikk klasse for sportsbiler som har noen unike egenskaper (f.eks. høyere hastighet eller mer aerodynamisk design).
Dette lar oss skrive mindre kode og gjøre den mer organisert, fordi vi ikke trenger å gjenta den samme koden for flere lignende klasser.
For å arve fra en klasse i Python, bruker vi nøkkelordet "class" og spesifiserer navnet på den eksisterende klassen i parenteser etter navnet på den nye klassen vår.



## Superklasse
I Python refererer superklassen til den eksisterende klassen som en ny klasse arver fra ved å bruke arv.
Når du arver fra en eksisterende klasse, vil den nye klassen inneholde alle egenskapene og metodene til superklassen. Disse egenskapene og metodene kan være tilgjengelige for den nye klassen ved å bruke nøkkelordet "super" og kalle på den aktuelle metoden eller egenskapen.
For eksempel, hvis du har en klasse kalt "Animal" med en metode kalt "eat", og du arver fra denne klassen for å lage en ny klasse kalt "Cat", kan du bruke superklassen "Animal" til å kalle "eat" metoden i den nye klassen ved hjelp av "super().eat()".
Ved å bruke superklassen på denne måten kan du unngå å skrive den samme koden flere ganger i forskjellige klasser, og gjør det lettere å vedlikeholde og oppdatere koden din.

### Eksempel på det over

````python
class Bruker:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med brukers epost
        fornavn: En stirng med brukers fornavn
        etternavn: En string med brukers etternavn


    """

    def __init__(self, epost, fornavn, etternavn):
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn
    def logg_inn(self):
        print(f"{self.epost} logget inn")
    def logg_ut(self):
        print(f"{self.epost} logget ut")

class Lærer(Bruker):
    """Superklasse for Lærere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med lærers epost
        fornavn: En stirng med lærers fornavn
        etternavn: En string med lærers etternavn
        lønnskonto: En string med lærers lønnskonto

    """
     
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto = lønnskonto
````