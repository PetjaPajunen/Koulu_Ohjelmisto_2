
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def __str__(self) -> str:
        return (f'Rekisteritunnus: {self.rekisteritunnus},\n'
                f'Huippunopeus: {self.huippunopeus} km/h,\n'
                f'Tämänhetkinen nopeus: {self.tamanhetkinen_nopeus} km/h,\n'
                f'Kuljettu matka: {self.kuljettu_matka} km')
    
if __name__ == "__main__":
    Auto = Auto("ABC-123", 142)
    print(f"\n{Auto}")