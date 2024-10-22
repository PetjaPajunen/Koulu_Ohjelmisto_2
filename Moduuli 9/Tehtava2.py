
class auto:
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

    def __str__(self) -> str:
        return (f'Rekisteritunnus: {self.rekisteritunnus},\n'
                f'Huippunopeus: {self.huippunopeus} km/h,\n'
                f'Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h,\n'
                f'Kuljettu matka: {self.kuljettu_matka} km')

    
if __name__ == "__main__":
    auto = auto("ABC-123", 142)
    speeds = [30, 70, 50]
    
    for i in speeds:
        auto.kiihdytä(i)
        print(auto)

    auto.kiihdytä(-200)
    print(f"!!Äkkijarrutus!! \nnopeus:{auto}")
    