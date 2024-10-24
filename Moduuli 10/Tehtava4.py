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

class kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, osallistujat):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            auto.kiihdytä(random.randint(-10,15))
            auto.kulje(1)
            
    def tulosta_tilanne(self, auto_lista):
        print("Jokaisen auton ominaisuudet lajiteltuna suoritusten perusteella:")
        auto_lista.sort(key=lambda x: x.kuljettu_matka, reverse=True) 
        for auto in auto_lista:       
                print(f"\nAuto: {auto.rekisteritunnus}")
                print("___________________________________")
                print(auto)
                print("___________________________________")
            

    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            if auto.kuljettu_matka > self.kilpailun_pituus:
                print(f"\n\n\n\nLoppu, auto {auto.rekisteritunnus} voitti")
                return True
            else:
                return False


osallistujat = []

for i in range(1,11):
            uusiAuto = (f"ABC-{i}", random.randint(100,200))
            osallistujat.append(Auto(uusiAuto[0], uusiAuto[1]))

k = kilpailu("Suuri romuralli", 8000, osallistujat)

tunti = 0
while True:
    k.tunti_kuluu()
    
    if tunti % 10 == 2:
        k.tulosta_tilanne(k.osallistujat)

    if k.kilpailu_ohi() == True:
        k.tulosta_tilanne(k.osallistujat)
        print(f"\nKilpailussa kesti {tunti}-tuntia")
        break
    tunti += 1
