import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = random.randint(100, self.huippunopeus)
        self.kuljettu_matka = 0

    

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, tunti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
        self.tunti = tunti

    def laske_kuljettu_matka(self):
        self.kuljettu_matka = self.tamanhetkinen_nopeus * self.tunti
        return self.kuljettu_matka
        
    def tulosta_tiedot(self):
        print(f'Rekisteritunnus: {self.rekisteritunnus},')
        print(f'Huippunopeus: {self.huippunopeus} km/h,')
        print(f'Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h,')
        print(f'Kuljettu matka: {self.kuljettu_matka} km')
        print(f'Akkukapasiteetti: {self.akkukapasiteetti} kW/h')



class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko, tunti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko
        self.tunti = tunti
        

    def laske_kuljettu_matka(self):
        self.kuljettu_matka = self.tamanhetkinen_nopeus * self.tunti
        return self.kuljettu_matka
        
    def tulosta_tiedot(self):
        print(f'Rekisteritunnus: {self.rekisteritunnus},')
        print(f'Huippunopeus: {self.huippunopeus} km/h,')
        print(f'Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h,')
        print(f'Kuljettu matka: {self.kuljettu_matka} km')
        print(f'Akkukapasiteetti: {self.bensatankin_koko} kW/h')

sähkö = Sähköauto("ABC-15", 180, 52.5, 3)
sähkö.laske_kuljettu_matka()
sähkö.tulosta_tiedot()

print("_______________________\n")

poltto = Polttomoottoriauto("ACD-123", 165, 32.3, 3)
poltto.laske_kuljettu_matka()
poltto.tulosta_tiedot()


""" print(f"Tämänhetkinen nopeus: {sähkö.tamanhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {sähkö.laske_kuljettu_matka()} km") """

"""
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

    def tulosta_tiedot(self):
        print (f'Rekisteritunnus: {self.rekisteritunnus}, 
        Huippunopeus: {self.huippunopeus} km/h, 
        Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h, 
        Kuljettu matka: {self.kuljettu_matka} km')
  
  """