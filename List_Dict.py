teman = {}
teman['nama']   = 'daffa'
teman['sex']    = 'laki2'
teman['umur']   = 6

teman2 = {}
teman2['nama']   = 'diva'
teman2['sex']    = 'perempuan'
teman2['umur']   = 3

temans = []
temans.append(teman)
temans.append(teman2)
print(temans)
print('Jumlah teman %d orang' % len(temans))
print('---')
for dt in temans:
    print(dt['nama'])
# print(teman[0]['umur'])