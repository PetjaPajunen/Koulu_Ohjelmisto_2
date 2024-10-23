
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + muutos
    
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunti):
        uusi_matka = self.tamanhetkinen_nopeus * tunti
        self.kuljettu_matka = uusi_matka

    def __str__(self) -> str:
        return (f'Rekisteritunnus: {self.rekisteritunnus},\n'
                f'Huippunopeus: {self.huippunopeus} km/h,\n'
                f'Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h,\n'
                f'Kuljettu matka: {self.kuljettu_matka} km')

    
if __name__ == "__main__":
    Auto = Auto("ABC-123", 142)
    speedsAndTimes = [(30, 1.5), (70, 2.5), (50, 3.5)]
    
    for i in speedsAndTimes:
        Auto.kiihdytä(i[0])
        Auto.kulje(i[1])
        print(f"\n{Auto}")

    Auto.kiihdytä(-200)
    print(f"\n!!Äkkijarrutus!! \n\nnopeus:{Auto}")