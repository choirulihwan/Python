class Teman:
    JUMLAH = 0
    def __init__(self, nama, sex):
        self.nama = nama
        self.sex = sex
        self.alamat = ''
        Teman.JUMLAH = Teman.JUMLAH + 1

    def __str__(self):
        if self.alamat == '':
            return ('Nama = %s, sex = %s' % (self.nama, self.sex))
        else:
            return ('Nama = %s, sex = %s, alamat = %s' % (self.nama, self.sex, self.alamat))

    def berbicara(self):
        print('Hai kamu, nama saya %s. kamu siapa?' % self.nama)

temans = []

temans.append(Teman('daffa', 'laki2'))
temans.append(Teman('diva', 'perempuan'))
temans.append(Teman('erna', 'perempuan'))

choirul = Teman('choirul', 'laki2')
choirul.alamat = 'Kasihan, Bantul'
choirul.berbicara()

temans.append(choirul)

print('Jumlah teman dengan fungi len = %d' % len(temans))
print('Jumlah teman dengan variable = %d' % Teman.JUMLAH)




# temans.append('daffa')
# temans.append('diva')
# temans.append('erna')
# temans.append('choirul')