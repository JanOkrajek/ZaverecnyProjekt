from poistenec import Poistenec
class Evidence:
    poistenci = []
    def __init__(self):
        self.poistenci = []

    def vloz(self, jmeno, prijmeni, vek, cislo):
        self.poistenci.append(Poistenec(jmeno, prijmeni, vek, cislo))

    def vypis(self):
        for poistenec in self.poistenci:
            print(poistenec)

    def vyhledat_poistenec(self, jmeno, prijmeni):
        for poistenec in self.poistenci:
            if poistenec.jmeno == jmeno and poistenec.prijmeni == prijmeni:
                return poistenec
        return None

    def __str__(self):
        return f"poistenec: {self.jmeno} {self.prijmeni}"