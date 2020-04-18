class Buku:
    JUMLAH = 0
    def __init__(self, judul, harga):
        self.judul = judul
        self.harga = harga
        self.penulis = ''
        Buku.JUMLAH = Buku.JUMLAH + 1

    def __str__(self):
        if self.penulis == '':
            return 'Judul = %s harganya = %d' % (self.judul, self.harga)
        else:
            return 'Judul = %s harganya = %d ditulis oleh %s'  % (self.judul, self.harga, self.penulis)



bukus = []
bukus.append(Buku('Dibawah lindungan ka\'bah', 40000))
bukus.append(Buku('Tenggelamnya kapal van der wick', 65000))
bukus.append(Buku('Dibawah lindungan ka\'bah', 40000))
pangeran = Buku('Sang pangeran dan janissary terakhir', 100000)
pangeran.penulis = 'Salim A fillah'
bukus.append(pangeran)

print('Jumlah buku = %d' % len(bukus))
print('Jumlah buku = %d' % Buku.JUMLAH)
# bukus.append('Dibawah lindungan ka\'bah')
# bukus.append('Tenggelamnya kapal van der wick')
# bukus.append('Digital fortress')
# bukus.append('Sang pangeran dan janissary terakhir')