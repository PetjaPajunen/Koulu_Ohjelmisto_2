
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print("\n", (len(self.kirjoittaja) + len(str(self.sivumaara)) + len(self.nimi) + 6) * "_")
        print(f"Kirjan nimi: {self.nimi} \nTekijä: {self.kirjoittaja} \nSivumäärä: {self.sivumaara}")
        print((len(self.kirjoittaja) + len(str(self.sivumaara)) + len(self.nimi) + 6) * "_", "\n")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja
    
    def tulosta_tiedot(self):
        print("\n", (len(self.paatoimittaja) + len(self.nimi) + 6) * "_")
        print(f"Lehden nimi: {self.nimi} \nPäätoimittaja: {self.paatoimittaja}")
        print((len(self.paatoimittaja) + len(self.nimi) + 6) * "_", "\n")


lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)


kirja.tulosta_tiedot()
lehti.tulosta_tiedot()