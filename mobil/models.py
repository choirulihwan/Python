class Mobil:
    def __init__(self, merk, cc, bb, jenis):
        self.merk = merk
        self.cc = cc
        self.bb = bb
        self.jenis = jenis

    def __str__(self):
        return '{} {} cc, bahan bakar {}'.format(self.merk, self.cc, self.bb, self.jenis)


mobil_saya = []

mobil1 = Mobil('avanza', 1300, 'pertalite', 'MVP')
mobil_saya.append(mobil1)

mobil_saya.append(Mobil('pajero', 2500, 'pertamax', 'SUV'))

