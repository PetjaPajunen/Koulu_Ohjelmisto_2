
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.taman_hetkinen_kerros = self.alin_kerros

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
            f"______________________________________________\n"
            f"| Hissin kerros: {self.taman_hetkinen_kerros},\n"
            f"| Hissin alin kerros: {self.alin_kerros},\n"
            f"| Hissin ylin kerros: {self.ylin_kerros}\n" 
            f"______________________________________________"
            )

h = Hissi(-2, 10)


h = Hissi(-2, 10)
h.siirry_kerrokseen(10)
print(h)

h.siirry_kerrokseen(-2)

print(h)