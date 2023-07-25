class Poistenec:

    jmeno = None
    prijmeni = None
    vek= None
    cislo = None

    def __init__(self, jmeno, prijmeni, vek, cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.cislo = cislo

    def __str__(self):
        return f"{self.jmeno.ljust(10)}{self.prijmeni.ljust(10)}{self.vek.ljust(10)}{self.cislo}"
    # poistenec(ak si dám f"poistenec:, vypíše to v riešeni aj to poistenec:)