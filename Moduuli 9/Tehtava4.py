import random


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
        self.kuljettu_matka += uusi_matka

    def __str__(self) -> str:
        return (f'| Rekisteritunnus: {self.rekisteritunnus},\n'
                f'| Huippunopeus: {self.huippunopeus} km/h,\n'
                f'| Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h,\n'
                f'| Kuljettu matka: {self.kuljettu_matka} km')

    
if __name__ == "__main__":
    autot = []
    tarkistaja = 0
    
    for i in range(1,11):
        uusiAuto = (f"ABC-{i}", random.randint(100,200))
        autot.append(Auto(uusiAuto[0], uusiAuto[1]))


    while 1 == 1:
        if tarkistaja > 9:
            tarkistaja = 0

        autot[tarkistaja].kiihdytä(random.randint(-10,15))
        autot[tarkistaja].kulje(1)

        if autot[tarkistaja].kuljettu_matka > 10000:
            print(f"\nLoppu, auto {autot[tarkistaja].rekisteritunnus} voitti \nJokaisen auton ominaisuudet lajiteltuna suoritusten perusteella:")
            
            autot.sort(key=lambda x: x.kuljettu_matka, reverse=True)

            for i in autot:
                print(f"\nAuto: {i.rekisteritunnus}")
                print("___________________________________")
                print(i)
                print("___________________________________")
            break

        tarkistaja = tarkistaja + 1
