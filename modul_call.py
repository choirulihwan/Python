from Listofdict import *

i = 0
print('mobil_saya: ')
for mobil in mobil_saya:
     i += 1
     print('{} : {} {} cc, bahan bakar {}'.format(i, mobil['merk'], mobil['cc'], mobil['bahan_bakar']))