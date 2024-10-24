
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, hissin_nimi):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.taman_hetkinen_kerros = self.alin_kerros
        self.hissin_nimi = hissin_nimi

    def siirry_kerrokseen(self, kerros):
        if kerros < self.taman_hetkinen_kerros:
            while kerros < self.taman_hetkinen_kerros:
                self.kerros_alas()

        elif kerros > self.taman_hetkinen_kerros:
            while kerros > self.taman_hetkinen_kerros:
                self.kerros_ylos()

    def kerros_ylos(self):
        uusi_kerros = self.taman_hetkinen_kerros + 1
        self.taman_hetkinen_kerros = uusi_kerros
    
    def kerros_alas(self):
        uusi_kerros = self.taman_hetkinen_kerros - 1
        self.taman_hetkinen_kerros = uusi_kerros
 
    def __str__(self) -> str:
        return(
            f"  Hissi {self.hissin_nimi}\n" 
            f"______________________________________________\n"
            f"| Hissin kerros: {self.taman_hetkinen_kerros},\n"
            f"| Hissin alin kerros: {self.alin_kerros},\n"
            f"| Hissin ylin kerros: {self.ylin_kerros}\n"
            f"______________________________________________"
            )


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara
        self.hissit = []
        for i in range(0, self.hissien_maara):
            hissi = Hissi(self.alin_kerros, self.ylin_kerros, i)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kerros):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kerros)
        print(hissi)



t = Talo(-2, 10, 2)
t.aja_hissia(0, 5)
t.aja_hissia(1, -2)