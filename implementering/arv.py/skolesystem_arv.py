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



class Faglærer(Lærer):
    """Superklasse for Faglærere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med faglærers epost
        fornavn: En stirng med faglærers fornavn
        etternavn: En string med faglærers etternavn
        lønnskonto: En string med faglærers lønnskonto
        kompetanse: En string med faglærers kompetanse
        klasser: En string med faglæreres klasser

    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse = []
        self.klasser = []

class Kontaktlærer(Lærer):
    """Superklasse for Kontaktlærere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med kontaktlærers epost
        fornavn: En stirng med kontaktlærers fornavn
        etternavn: En string med kontaktlærers etternavn
        lønnskonto: En string med kontaktlærers lønnskonto
        klasse: En string med kontaktlærers klasse
        trinn: En int med kontaktlærers trinn

    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.klasse = klasse
        self.trinn = trinn

class Elev(Bruker):
    """Superklasse for Elever i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med elevers epost
        fornavn: En stirng med elevers fornavn
        etternavn: En string med elevers etternavn
        trinn: En int med elevers trinn
        klasse: En string med elevers klasse
        fag: En liste med elevers fag

    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse,):
        super().__init__(epost, fornavn, etternavn)
        self.trinn = trinn
        self.klasse = klasse
        self.fag = []

# Denne brukes for testing, betyr at koden inne i if-setningen kun kjøres hvis vi "trykker play" på denne filen eller kjører denne fila i terminalen
if __name__ == "__main__":
    ravi = Lærer("ravi@viken.no", "david Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()

    chinga = Elev("chingac@viken.no", "Chinga", "Chong", 2, "STG")
    chinga.logg_inn()